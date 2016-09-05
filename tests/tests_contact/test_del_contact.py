from Model.contacts import Contacts

def test_del_contact(app):
    if app.contacts.count() == 0:
        app.contacts.add(Contacts(first_name='Vasya',last_name='Pupkin',initials='VP'))
    app.contacts.delete()
