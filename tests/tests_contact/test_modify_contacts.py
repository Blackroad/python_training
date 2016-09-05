from Model.contacts import Contacts


def test_modify_contacts_first_name(app):
    if app.contacts.count() == 0:
        app.contacts.add(Contacts(first_name='Igor',last_name='Rogi',email='rogi@gmail.com'))
    app.contacts.modify(Contacts(first_name = 'Vasya'))



def test_modify_contacts_last_name(app):
   app.contacts.modify(Contacts(last_name ='Adam'))
