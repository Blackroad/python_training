# -*- coding: utf-8 -*-
from Model.contacts import Contacts


def test_add_contact(app):
    app.contacts.add(Contacts(first_name='John', last_name='Smyth', initials='JS', nickname='johny', home_phone='123123', email='jo@gmnail.com'))
    app.session.logout()


def test_add_empty_contact(app):
    app.contacts.add(Contacts(first_name='', last_name='', initials='', nickname='', home_phone='', email=''))






