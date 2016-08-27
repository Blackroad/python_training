# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from Model.contacts import Contacts


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.add_new_contact(Contacts(first_name='John',last_name='Smyth',initials='JS',nickname='johny',home_phone='123123',email='jo@gmnail.com'))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.add_new_contact(Contacts(first_name='',last_name='',initials='',nickname='',home_phone='',email=''))





