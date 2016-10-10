from Model.group import Group
import random


def test_modify_group_name(app,db,check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='real',header = 'true'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    modified_group = Group(name='modified')
    modified_group.id = group.id
    app.group.modify_group_by_id(group.id, modified_group)
    new_groups = db.get_group_list()
    assert len(old_groups) == app.group.count()
    if check_ui:
       assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_modify_group_header(app):
    #old_groups = app.group.get_group_list()
    #app.group.modify_first_group(Group(header='modified'))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)