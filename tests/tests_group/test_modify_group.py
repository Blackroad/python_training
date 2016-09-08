from Model.group import Group


def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    modified_group = Group(name='modified')
    group = Group(name='real',header = 'true')
    modified_group.id = old_groups[0].id
    if app.group.count() == 0:
        app.group.create(group)
    app.group.modify_first_group(modified_group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = modified_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
    #old_groups = app.group.get_group_list()
    #app.group.modify_first_group(Group(header='modified'))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)