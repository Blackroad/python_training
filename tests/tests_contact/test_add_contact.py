# -*- coding: utf-8 -*-
from Model.contacts import Contacts
import pytest
import random
import string

def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contacts(first_name='ADt',last_name='vadddda',nickname='fsse',home_phone='Home[123441]',
                       workphone='+work(231241)', mobilephone='m127-331-233', fax = 'fax21737', secondaryphone= '+33123',
                       address='london st123,ap2',address2='New York ap123',
                       email='email144@gmail.com',email2='email123@gmail.com',email3='email3@yandex.ru') for x in range(2)] + \
           [Contacts(first_name='', last_name='', initials='', nickname='', home_phone='', email='')
            for y in range(2)]

@pytest.mark.parametrize("contact",testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app,contact):
    old_contacts = app.contacts.get_contact_list()
    app.contacts.add(contact)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)









