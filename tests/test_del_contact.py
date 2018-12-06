from model.contact import Contact

def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Natasha", lastname="Wilson"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_contact()
    new_contact = app.contact.get_contacts_list()
    assert len(old_contacts) -1 == len(new_contact)
    old_contacts[0:1]= []
    assert old_contacts == new_contact

