from model.group import Group


def test_modify_group_name(app):
    if app.group.count()==0:
        app.group.create(Group(name="tobemodify"))
    app.group.modify_first_group(Group(name="Lavanda_tree"))


def test_modify_group_header(app):
    if app.group.count()==0:
        app.group.create(Group(name="tobemodify", footer = "mofifyfooter"))
    app.group.modify_first_group(Group(footer="updatedValue"))

