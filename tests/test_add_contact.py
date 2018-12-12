# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="Coconut",
                      middlename="longTree",
                      lastname="Borisovich",
                      nickname="borka",
                      companyname="boOne",
                      address="23Kittiwake drive",
                      email="borka@mail.com",
                      home="+67464646464",
                      mobile="(3212)58768",
                      work="77-54-564-56",
                      phone2="425 3616 6163 416")
    app.contact.create(contact)
    assert len(old_contacts)+1 == app.contact.count()
    new_contact = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)





