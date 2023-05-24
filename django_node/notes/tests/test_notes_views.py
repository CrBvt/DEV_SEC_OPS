""" Notes tests """

import pytest

# from django.contrib.auth.models import User

# from notes.models import Notes
from notes.tests.factories import UserFactory, NoteFactory

@pytest.fixture
def logged_user(client):
    """
    *TEST*
    Fixture that provides an authenticated user

    :param client: pytest-django default client fixture
    """
    user = UserFactory()
    client.login(username=user.username, password='password')

    return user

@pytest.mark.django_db
def test_list_endpoint_authenticated(client, logged_user):
    """
    *TEST*
    Accessing the /smart/notes endpoint with an authenticated user returns its notes

    :param client: pytest-django default client fixture
    :param logged_user: authenticated user fixture
    """

    note_1 = NoteFactory(user=logged_user)
    note_2 = NoteFactory(user=logged_user)

    response = client.get(path='/smart/notes', follow=True)
    assert 200 == response.status_code
    content = str(response.content)
    assert note_1.title in content
    assert note_2.title in content
    assert 2 == content.count('<h3>')

@pytest.mark.django_db
def test_list_endpoint_user_notes_only(client, logged_user):
    """
    *TEST*
    Accessing the /smart/notes endpoint with an authenticated user returns its notes
    and not another user's note

    :param client: pytest-django default client fixture
    :param logged_user: authenticated user fixture
    """

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


@pytest.mark.django_db
def test_create_endpoint_authenticated(client, logged_user):
    """
    *TEST*
    Posting a matching form data to the /smart/notes/new endpoint with an authenticated user
    creates the note for the user

    :param client: pytest-django default client fixture
    :param logged_user: authenticated user fixture
    """

    form_data = {
        'title': 'big title',
        'text': 'big_text'
    }

    response = client.post('/smart/notes/new', form_data, follow=True)

    assert 200 == response.status_code
    assert 'notes/notes_list.html' in response.template_name
    assert 1 == logged_user.notes.count()
    assert "big title" == logged_user.notes.first().title
