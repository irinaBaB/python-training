from model.contact import Contact


def test_modify_contact_firstname(app):
    app.group.modify_first_contact(Contact(firstname="Natasha"))


def test_modify_contact_lastname(app):
        app.group.modify_first_contact(Contact(lastname="Wilson"))


def test_modify_contact_dateofbirth(app):
    app.group.modify_first_contact(Contact(dateofbirth="Wilson"))