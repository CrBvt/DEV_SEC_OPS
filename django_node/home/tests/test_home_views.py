""" Tests for Home app """

import pytest

from django.contrib.auth.models import User


def test_home_endpoint(client):
    """*TEST*
    Accessing the /home endpoint returns the welcome.html page

    :param client: pytest-django default client fixture
    """
    response = client.get(path='/')
    assert 200 == response.status_code
    assert 'DEV_SEC_OPS' in str(response.content)


def test_signup_endpoint_unauthenticated(client):
    """*TEST*
    Accessing the /signup endpoint with an unauthenticated user returns form for signing-up

    :param client: pytest-django default client fixture
    """
    # Unauthenticated
    response = client.get(path='/signup')
    assert 200 == response.status_code
    assert 'home/register.html' in str(response.template_name)


@pytest.mark.django_db
def test_signup_endpoint_authenticated(client):
    """*TEST*
    Accessing the /signup endpoint with an authenticated user redirects to its dashboard

    :param client: pytest-django default client fixture
    """
    # Authenticated
    user = User.objects.create_user('TestUser', 'fake@example.com', 'password')
    client.login(username=user.username, password='password')
    response = client.get(path='/signup', follow=True)
    assert 200 == response.status_code
    print(response.template_name)
    assert 'notes/notes_list.html' in str(response.template_name)
