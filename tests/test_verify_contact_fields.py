from model.contact import Contact
from random import randrange
import re

def test_verify_contact_details_by_index(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Natasha", lastname="Wilson",
                                   email='superlight@maui.com',
                                   email2 = 'christmascake@gmail.com',
                                   email3 = 'winterforest@hotmailcom',
                                   address = '1 quarterly drive, Pinehill',
                                   home = "(57876)5789867",
                                   work = '+34689567987',
                                   mobile = '021-45-3234-3454',
                                   phone2 = '467 67876 67876'))
    index = randrange(app.contact.count())
    contact_list_home_page = app.contact.get_contacts_list()[index]
    contact_list_from_edit_page = app.contact.get_contacts_from_edit_page(index)
    assert contact_list_home_page.firstname == contact_list_from_edit_page.firstname
    assert contact_list_home_page.lastname == contact_list_from_edit_page.lastname
    assert contact_list_home_page.address == contact_list_from_edit_page.address
    assert contact_list_home_page.all_phones_from_home_page == merge_phone_from_edit_page(contact_list_from_edit_page)
    assert contact_list_home_page.all_emails_from_home_page == merge_emails_from_edit_page(contact_list_from_edit_page)

def clear(s):
   return re.sub("[() -]","",s)


def merge_phone_from_edit_page(contact):
    return "\n".join (filter(lambda x: x!="",
                            map(lambda x: clear(x),filter (lambda x: x is not None,
                                                           [contact.home,contact.mobile,contact.work,contact.phone2]))))

def merge_emails_from_edit_page(contact):
    return "\n".join (filter(lambda x: x!="",
                            map(lambda x: clear(x),filter (lambda x: x is not None,
                                                           [contact.email,contact.email2,contact.email3]))))




