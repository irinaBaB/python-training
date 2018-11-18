from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Natasha", lastname="Wilson"))
    app.contact.delete_contact()
