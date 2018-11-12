from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="test123", header="fgfgfgfgf", footer="ffgfgfgfg"))
    app.session.logout()
