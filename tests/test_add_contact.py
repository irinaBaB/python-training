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
                      phone2="67464646464")
    app.contact.create(contact)
    new_contact = app.contact.get_contacts_list()
    assert len(old_contacts)+1 == len(new_contact)





