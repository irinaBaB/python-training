from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="SomeRandom", lastname="contact"))
    app.contact.modify_first_contact(Contact(firstname="Natasha"))


def test_modify_contact_lastname(app):
    app.contact.modify_first_contact(Contact(lastname="Wilson"))


def test_modify_contact_mobilephone(app):
    app.contact.modify_first_contact(Contact(mobile="07845670"))