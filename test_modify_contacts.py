from Model.contacts import Contacts
from random import randrange


def test_modify_contacts_first_name(app):

   if app.contacts.count() == 0:
        contacts = Contacts(first_name='Igor', last_name='Petro')
        app.contacts.add(contacts)
   old_contacts = app.contacts.get_contact_list()
   index = randrange(len(old_contacts))
   modified_contact = Contacts(first_name ='1sad',last_name='edited')
   modified_contact.id = old_contacts[index].id
   app.contacts.modify_contact_by_index(index, modified_contact)
   new_contacts = app.contacts.get_contact_list()
   assert len(old_contacts) == app.contacts.count()
   old_contacts[index] = modified_contact
   assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)

#def test_modify_contacts_last_name(app):
#   app.contacts.modify(Contacts(last_name ='Adam'))
