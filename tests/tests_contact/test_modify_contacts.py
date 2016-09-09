from Model.contacts import Contacts


def test_modify_contacts_first_name(app):
   old_contacts = app.contacts.get_contact_list()
   contact = Contacts(first_name='Igor',last_name='Petro')
   modified_contact = Contacts(first_name ='Peppa')
   modified_contact.id = old_contacts[0].id
   if app.contacts.count() == 0:
        app.contacts.add(contact)
   app.contacts.modify(modified_contact)
   new_contacts = app.contacts.get_contact_list()
   assert len(old_contacts) == len(new_contacts)
   old_contacts[0] = modified_contact
   assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)

#def test_modify_contacts_last_name(app):
#   app.contacts.modify(Contacts(last_name ='Adam'))
