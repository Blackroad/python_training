from Model.contacts import Contacts
import random


def test_del_contact(app,db):
    if len (db.get_contact_list()) == 0:
        app.contacts.add(Contacts(first_name='Vasya',last_name='Pupkin',initials='VP'))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contacts.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == app.contacts.count()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)

