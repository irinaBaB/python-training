# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Coconut", middlename="longTree", lastname="Borisovich", nickname="bor'ka",companyname="boOne", address="23Kittiwake drive", email="borka@mail.com", phone2="67464646464"))
    app.logout()


def tearDown(app):
    app.destroy()


if __name__ == "__main__":
    unittest.main()
