from Model.contacts import Contacts
import random

def test_modify_contacts_first_name(app,db,check_ui):
   if len(db.get_contact_list()) == 0:
        contacts = Contacts(firstname='Igor', lastname='Petro')
        app.contacts.add(contacts)
   old_contacts = db.get_contact_list()
   contact = random.choice(old_contacts)
   modified_contact = Contacts(firstname='1sad', lastname='edited')
   modified_contact.id = contact.id
   app.contacts.modify_contact_by_id(contact.id, modified_contact)
   new_contacts = db.get_contact_list()
   assert len(old_contacts) == app.contacts.count()
   if check_ui:
      assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.contacts.get_contact_list(), key=Contacts.id_or_max)

#def test_modify_contacts_last_name(app):
#   app.contacts.modify(Contacts(last_name ='Adam'))
