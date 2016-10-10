from Model.contacts import Contacts


def test_contact_list(app,db):
    ui_list = app.contacts.get_contact_list()

    def clean(contact):
        return Contacts(id=contact.id,firstname = contact.firstname.strip(),
                        lastname=contact.lastname.strip(),address=contact.address.strip(),
                        all_emails_from_home_page=(contact.email + contact.email2 + contact.email3).strip(),
                        all_phones_from_home_page=(contact.homephone + contact.mobilephone +
                                                   contact.workphone + contact.secondaryphone).strip())

    db_list = map(clean,db.get_contact_list())
    assert sorted(ui_list, key=Contacts.id_or_max) == sorted(db_list, key=Contacts.id_or_max)