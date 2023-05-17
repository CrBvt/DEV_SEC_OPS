import pytest

from django.contrib.auth.models import User

from notes.models import Notes

@pytest.fixture
def logged_user(client):
    user = User.objects.create_user('user', 'user@example.com', 'password')
    client.login(username=user.username, password='password')

    return user

@pytest.mark.django_db
def test_list_endpoint_returns_user_notes(client, logged_user):

    note = Notes.objects.create(title='An interesting title', text='', user=logged_user)
    note = Notes.objects.create(title='A new title', text='', user=logged_user)

    response = client.get(path='/smart/notes', follow=True)
    assert 200 == response.status_code
    content = str(response.content)
    assert "An interesting title" in content
    assert "A new title" in content
    assert 2 == content.count('<h3>')

@pytest.mark.django_db
def test_list_endpoint_returns_only_user_notes_from_authenticated_user(client, logged_user):

    another_user = User.objects.create_user('another_user', 'another@example.com', 'password')
    Notes.objects.create(title='Fake Note', text='', user=another_user)

    Notes.objects.create(title='An interesting title', text='', user=logged_user)
    Notes.objects.create(title='A new title', text='', user=logged_user)

    response = client.get(path='/smart/notes', follow=True)
    assert 200 == response.status_code
    content = str(response.content)
    assert "An interesting title" in content
    assert "A new title" in content
    assert 2 == content.count('<h3>')
    assert 'Fake Note' not in content
