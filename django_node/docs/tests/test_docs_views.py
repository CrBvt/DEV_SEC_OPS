""" Tests for Docs app """
import json


def test_docs_endpoint(client):
    """*TEST*
    Accessing the /docs endpoint returns the read-the-docs index.html page

    :param client: pytest-django default client fixture
    """

    response = client.get(path='/smart/docs/', follow=True)
    assert 200 == response.status_code
    assert 'index.html' in response.headers['Content-Disposition'].split('filename=')[1].strip('\"')
