# -*- coding: utf-8 -*-
import random
from fixture.group import Group
from fixture.contacts import Contacts
from fixture.orm import ORMFixture

db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')

def test_add_contact_to_group(app,json_contacts,json_groups):
     groups_container = json_groups
     if len(db.get_group_list())==0:
          app.group.create(groups_container)
     groups_n = random.choice(db.get_group_list())
     contacts_container = json_contacts
     if len(db.get_contact_list())==0 or len(db.get_contacts_not_in_group(Group(id='%s' % groups_n.id)))==0:
         app.contacts.add(contacts_container)
     list_contacts = db.get_contacts_in_group(Group(id='%s' % groups_n.id))
     contact = random.choice(db.get_contacts_not_in_group(Group(id='%s' % groups_n.id)))
     app.contacts.add_to_group(contact.id,groups_n.id)
     list_contacts.append(contact)
     new_list_contacts = db.get_contacts_in_group(Group(id='%s' % groups_n.id))
     assert sorted(list_contacts, key=Contacts.id_or_max) == sorted(new_list_contacts, key=Contacts.id_or_max)

