from Model.contacts import Contacts

def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.modify(Contacts(first_name='Adam', last_name='West', initials='AW', nickname='Ad', home_phone='123123441', email='west_ad@gmnail.com'))
    app.session.logout()