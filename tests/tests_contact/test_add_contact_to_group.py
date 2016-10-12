# -*- coding: utf-8 -*-
import random
from fixture.group import Group
from fixture.orm import ORMFixture


def test_add_contact_to_group(app,db):
    db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')
    old_contacts = db.get_contacts_in_group(Group(id='24'))
    contact = random.choice(db.get_contact_list())
    app.contacts.add_to_group(contact.id)
    old_contacts.append(contact)
    new_contacts = db.get_contacts_in_group(Group(id='24'))
    assert sorted(old_contacts, key=Group.id_or_max) == sorted(new_contacts, key=Group.id_or_max)

    #old_contacts.append(contact)
    #assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)
