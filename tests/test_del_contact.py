from model.contact import Contact
from random import randrange
import time


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Natasha", lastname="Wilson"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contact = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contact)
    old_contacts[index:index + 1] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)




