# -*- coding: utf-8 -*-
from Model.contacts import Contacts


def test_add_contact(app):
    old_contacts = app.contacts.get_contact_list()
    contact = Contacts(first_name='First',last_name='vasia',nickname='fsse',home_phone='Home[123441]',
                       workphone='+work(231241)', mobilephone='m127-331-233', fax = 'fax21737', secondaryphone= '+33123')
    app.contacts.add(contact)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)


#def test_add_empty_contact(app):
   # old_contacts = app.contacts.get_contact_list()
   # contact = Contacts(first_name='', last_name='', initials='', nickname='', home_phone='', email='')
   # app.contacts.add(contact)
   # new_contacts = app.contacts.get_contact_list()
   # assert len(old_contacts) + 1 == len(new_contacts)
   # old_contacts.append(contact)
   # assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)






