# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string (prefix,maxlen):
    symbols=string.ascii_letters+string.digits + " "*10
    return prefix + "".join([random.choice(symbols)for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="Coconut",
                      middlename="longTree",
                      lastname="Borisovich",
                      nickname="borka",
                      companyname="boOne",
                      address="23Kittiwake drive",
                      email="borka@mail.com",
                      home="+67464646464",
                      mobile="(3212)58768",
                      work="77-54-564-56",
                      phone2="425 3616 6163 416")] + [

            Contact(firstname="Lana",
                      middlename="Sole",
                      lastname="Mavel",
                      nickname="most",
                      companyname="noname",
                      address="16 StoleRoad",
                      email="lanasole@gmail.com",
                      email2 = "sad@gmail.com",
                      email3 = "workmail@mail.ru",
                      home="45673563765",
                      mobile="(345)5323232",
                      work="+77-54-564-56",
                      phone2="(425) 3616 6163 416")] + [
    Contact(firstname = random_string("firstname", 13),middlename=random_string("middlename", 16),
            lastname = random_string("lastname",17),nickname =random_string("nickname",20), companyname= random_string("companyname",20),
            address=random_string("address", 20),email=random_string("email", 20),email2=random_string("email2", 20),
            email3=random_string("email3", 20),home=random_string("home", 20),mobile=random_string("mobile", 20),work=random_string("work", 20),
            phone2=random_string("phone2", 20))
    for i in range (7)
]


@pytest.mark.parametrize("contact", testdata,ids= [repr(x) for x in testdata])
def test_create_contact(app,contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts)+1 == app.contact.count()
    new_contact = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)





