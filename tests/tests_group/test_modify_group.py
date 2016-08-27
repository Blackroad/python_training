from Model.group import Group

def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_group(Group( name = 'updated_name', header = 'updated_heared', footer = 'updated_footer'))
    app.session.logout()