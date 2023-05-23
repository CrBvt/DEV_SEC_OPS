""" Notes tests object factory """

import factory
from factory import fuzzy

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from notes.models import Notes


class UserFactory(factory.django.DjangoModelFactory):
    """ Create a user for testing purpose """

    class Meta:
        """ DjangoModelFactory Meta for a user"""
        model = User

    username = factory.sequence(lambda n: f"user_{n:04}")
    email = factory.LazyAttribute(lambda user: f"{user.username}@example.com")
    password = factory.LazyFunction(lambda: make_password('password'))


class NoteFactory(factory.django.DjangoModelFactory):
    """ Create a note for testing purpose """
    class Meta:
        """ DjangoModelFactory Meta for a note"""
        model = Notes

    title = fuzzy.FuzzyText(length=20)
    text = fuzzy.FuzzyText(length=200)
    user = factory.SubFactory(UserFactory)
