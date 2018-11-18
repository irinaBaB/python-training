# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    app.contact.create(Contact(firstname="Coconut", middlename="longTree", lastname="Borisovich", nickname="borka", companyname="boOne", address="23Kittiwake drive", email="borka@mail.com", phone2="67464646464"))


