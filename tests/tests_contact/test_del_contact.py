def test_del_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.delete()
    app.session.logout()