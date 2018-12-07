from model.group import Group
from random import randrange

def test_modify_group_name(app):
    group = Group(name="tobemodify")
    if app.group.count()==0:
        app.group.create(group)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    modifygr= Group(name="Lavanda_tree")
    modifygr.id = old_groups[index].id
    app.group.modify_group_by_index(index,modifygr)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = modifygr
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#
# def test_modify_group_header(app):
#     if app.group.count()==0:
#         app.group.create(Group(name="tobemodify", footer = "mofifyfooter"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(footer="updatedValue"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
