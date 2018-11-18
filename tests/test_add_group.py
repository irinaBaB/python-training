# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="test123", header="fgfgfgfgf", footer="ffgfgfgfg"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

