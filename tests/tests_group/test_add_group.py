# -*- coding: utf-8 -*-

from Model.group import Group


def test_add_group(app):
    app.group.create(Group(name="new1", header="new2", footer="new3"))



def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

