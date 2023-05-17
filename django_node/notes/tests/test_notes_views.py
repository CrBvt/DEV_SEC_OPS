import pytest

from django.contrib.auth.models import User

from notes.models import Notes
from notes.tests.factories import UserFactory, NoteFactory

@pytest.fixture
def logged_user(client):
    user = UserFactory()
    client.login(username=user.username, password='password')

    return user

@pytest.mark.django_db
def test_list_endpoint_returns_user_notes(client, logged_user):

    note_1 = NoteFactory(user=logged_user)
    note_2 = NoteFactory(user=logged_user)

    response = client.get(path='/smart/notes', follow=True)
    assert 200 == response.status_code
    content = str(response.content)
    assert note_1.title in content
    assert note_2.title in content
    assert 2 == content.count('<h3>')

@pytest.mark.django_db
def test_list_endpoint_returns_only_user_notes_from_authenticated_user(client, logged_user):

    note_user_1 = NoteFactory(user=logged_user)
    note_user_2 = NoteFactory(user=logged_user)

    another_user = UserFactory()
    note_another_user = NoteFactory(user=another_user)

    response = client.get(path='/smart/notes', follow=True)

    assert 200 == response.status_code
    content = str(response.content)

    assert note_user_1.title in content
    assert note_user_2.title in content
    assert 2 == content.count('<h3>')

    assert note_another_user.title not in content
