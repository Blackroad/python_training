from pytest_bdd import given, when, then
from Model.contacts import Contacts
import random

#add contact
@given('a contact list')
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <firstname>, <lastname> and <nickname>')
def new_contact( firstname, lastname, nickname ):
    return Contacts(firstname = firstname, lastname=lastname, nickname=nickname)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contacts.add(new_contact)


@then('the new contact list is equal to the old list with the added contact')
def verify_new_contact(db,contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)

#delete contact
@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contacts.add(Contacts(firstname='Vasia', lastname='Vetrov'))
    return db.get_contact_list()

@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list')
def delete_contact(app,random_contact):
    app.contacts.delete_contact_by_id(random_contact.id)


@then('the new contact list is equal to the old list without deleted contact')
def verify_deleted_contact(app,random_contact,non_empty_contact_list, check_ui, db):
    old_contacts = non_empty_contact_list
    assert len(old_contacts) - 1 == app.contacts.count()
    old_contacts.remove(random_contact)
    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.contacts.get_group_list(),
                                                                      key=Contacts.id_or_max)




#modify
#re-use non_empty_contact_list, random_contact

@when('I modify the contact from the list with next contact data <firstname>, <lastname>')
def modify_contact(app,random_contact):
    app.contacts.modify_contact_by_id(random_contact.id, Contacts(firstname='Lin', lastname='Quer'))

@then('list with modified contact list is equal to the old list with not modified contact')
def verify_modified_contact_list(app,db,check_ui,non_empty_contact_list):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.contacts.get_contact_list(),
                                                                      key=Contacts.id_or_max)