from model.contact import Contact
from random import randrange


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="SomeRandom", lastname="container"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    field_change = Contact(firstname="babushka")
    field_change.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index,field_change)
    new_contact = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contact)
    old_contacts[index]= field_change
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


def test_modify_contact_lastname(app):
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    field_change = Contact(lastname="torpeda")
    field_change.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index,field_change)
    new_contact = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contact)
    old_contacts[index] = field_change
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


# def test_modify_contact_mobilephone(app):
#     old_contacts = app.contact.get_contacts_list()
#     field_change = Contact(mobile="07845670")
#     app.contact.modify_first_contact(field_change)
#     new_contact = app.contact.get_contacts_list()
#     assert len(old_contacts) == len(new_contact)