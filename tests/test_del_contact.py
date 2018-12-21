from model.contact import Contact
import random
import time


def test_delete_contact(app,db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Natasha", lastname="Wilson"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    #index = randrange(len(old_contacts))
    app.contact.delete_contact_by_id(contact.id)
    new_contact = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contact)
    old_contacts.remove(contact)
    assert old_contacts == new_contact
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)




