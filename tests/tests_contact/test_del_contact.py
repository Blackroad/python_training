from Model.contacts import Contacts
from random import randrange


def test_del_contact(app):
    if app.contacts.count() == 0:
        app.contacts.add(Contacts(first_name='Vasya',last_name='Pupkin',initials='VP'))
    old_contacts = app.contacts.get_contact_list()
    index = randrange(len(old_contacts))
    app.contacts.delete_contact_by_index(index)
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)

