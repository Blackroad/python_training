from Model.contacts import Contacts

def test_del_contact(app):
    old_contacts = app.contacts.get_contact_list()
    if app.contacts.count() == 0:
        app.contacts.add(Contacts(first_name='Vasya',last_name='Pupkin',initials='VP'))
    app.contacts.delete()
    new_contacts = app.contacts.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)

