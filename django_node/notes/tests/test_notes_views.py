import pytest

from django.contrib.auth.models import User

from notes.models import Notes

@pytest.mark.django_db
def test_list_endpoint_returns_user_notes(client):

    user = User.objects.create_user('user', 'user@example.com', 'password')
    client.login(username=user.username, password='password')

    note = Notes.objects.create(title='An interesting title', text='', user=user)
    note = Notes.objects.create(title='A new title', text='', user=user)

    response = client.get(path='/smart/notes', follow=True)
    assert 200 == response.status_code
    content = str(response.content)
    assert "An interesting title" in content
    assert "A new title" in content
    assert 2 == content.count('<h3>')

@pytest.mark.django_db
def test_list_endpoint_returns_only_user_notes_from_authenticated_user(client):

    another_user = User.objects.create_user('another_user', 'another@example.com', 'password')
    Notes.objects.create(title='Fake Note', text='', user=another_user)

    user = User.objects.create_user('user', 'user@example.com', 'password')
    client.login(username=user.username, password='password')

    Notes.objects.create(title='An interesting title', text='', user=user)
    Notes.objects.create(title='A new title', text='', user=user)

    response = client.get(path='/smart/notes', follow=True)
    assert 200 == response.status_code
    content = str(response.content)
    assert "An interesting title" in content
    assert "A new title" in content
    assert 2 == content.count('<h3>')
    assert 'Fake Note' not in content
