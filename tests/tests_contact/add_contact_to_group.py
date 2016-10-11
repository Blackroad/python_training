# -*- coding: utf-8 -*-
from Model.contacts import Contacts
import random


def test_add_contact_to_group(app, orm):
    old_contacts = orm.get_contacts_not_in_group()
    contact = random.choice(old_contacts)
    app.contacts.add_to_group(contact.id)
    #new_contacts = orm.get_contact_list()
    #old_contacts.append(contact)
    #assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)
