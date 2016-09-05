from Model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test',header='test2'))
    app.group.modify_first_group(Group(name='real'))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header='modified'))
