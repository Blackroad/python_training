# -*- coding: utf-8 -*-
from Model.contacts import Contacts
import pytest
import random
import string


def random_string(prefix,maxlen,symbols=None,digits=None):
    if symbols != None:
        symbols = string.ascii_letters + " "*10
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    elif digits !=None:
        digits = string.digits + "-"*3
        return prefix + "".join([random.choice(digits) for i in range(random.randrange(maxlen))])
    else:
        all = string.ascii_letters + string.digits +  string.punctuation + " "*10
        return prefix + "".join([random.choice(all) for i in range(random.randrange(maxlen))])

testdata = [Contacts(first_name=random_string('name',10),last_name=random_string('s_name',7),
                     nickname=random_string('n_name',6,symbols=1),
                     home_phone=random_string('phone',5,digits=1),
                     workphone=random_string('w_phone',5,digits=1),
                     mobilephone=random_string('m_phone',5,digits=1),
                     fax = random_string('n_name',6,digits=1),
                     secondaryphone= random_string('s_phone',6,digits=1),
                     address= random_string('address',6),
                     address2= random_string('address2',6),
                     email= random_string('mail1@',6),
                     email2= random_string('mail2@',6),
                     email3= random_string('mail3@',6))
            for x in range(2)] + [Contacts(first_name='', last_name='', initials='', nickname='', home_phone='', email='')
            for y in range(2)]

@pytest.mark.parametrize("contact",testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app,contact):
    old_contacts = app.contacts.get_contact_list()
    app.contacts.add(contact)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)









