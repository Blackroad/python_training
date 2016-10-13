import random
from fixture.group import Group
from fixture.contacts import Contacts
from fixture.orm import ORMFixture

db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')

def test_del_contact_from_group(app):
     groups_random = random.choice(db.get_group_list())
     if len(db.get_contacts_in_group(Group(id='%s' % groups_random.id)))==0:
         app.open_home_page()
         empty_contact = random.choice(db.get_contacts_not_in_group(Group(id='%s' % groups_random.id)))
         app.contacts.add_to_group(empty_contact.id, groups_random.id)
     app.contacts.select_group_for_contact_deletion_by_id(groups_random.id)
     list_contacts = db.get_contacts_in_group(Group(id='%s' % groups_random.id))
     contact_s = random.choice(db.get_contacts_in_group(Group(id='%s' % groups_random.id)))
     app.contacts.del_from_group_by_id(contact_s.id)
     list_contacts.remove(contact_s)
     new_list_contacts = db.get_contacts_in_group(Group(id='%s' % groups_random.id))
     assert list_contacts == new_list_contacts
    