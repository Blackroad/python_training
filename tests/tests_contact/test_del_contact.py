from Model.contacts import Contacts
import random
import pytest



def test_del_contact(app,db,check_ui):
    if len (db.get_contact_list()) == 0:
        app.contacts.add(Contacts(firstname='Vasya', lastname='Pupkin', initials='VP'))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contacts.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contacts.count()
    old_contacts.remove(contact)
    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.contacts.get_group_list(), key=Contacts.id_or_max)

