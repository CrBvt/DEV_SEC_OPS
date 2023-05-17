import pytest

from django.contrib.auth.models import User

def test_home_endpoint_returns_welcome_page(client):
    response = client.get(path='/')
    assert 200 == response.status_code
    assert 'DEV_SEC_OPS' in str(response.content)


def test_signup_endpoint_returns_form_for_unauthenticated_user(client):

    # Unauthenticated
    response = client.get(path='/signup')
    assert 200 == response.status_code
    assert 'home/register.html' in str(response.template_name)


@pytest.mark.django_db
def test_signup_endpoint_redirects_authenticated_user(client):
    """
        When a user is authenticated and try to access the sign-yp page,
        they are redirected to the list of their Notes
    """
    # Authenticated
    user = User.objects.create_user('TestUser', 'fake@example.com', 'password')
    client.login(username=user.username, password='password')
    response = client.get(path='/signup', follow=True)
    assert 200 == response.status_code
    print(response.template_name)
    assert 'notes/notes_list.html' in str(response.template_name)