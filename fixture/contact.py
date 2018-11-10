

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def return_to_homepage(self):
            wd = self.app.wd
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
            # create contact
            wd = self.app.wd
            # open contact page
            self.open_create_contact_page()
            wd.find_element_by_name("firstname").click()
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(contact.firstname)
            wd.find_element_by_name("middlename").click()
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys(contact.middlename)
            wd.find_element_by_name("lastname").click()
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(contact.lastname)
            wd.find_element_by_name("nickname").click()
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(contact.nickname)
            wd.find_element_by_name("company").click()
            wd.find_element_by_name("company").clear()
            wd.find_element_by_name("company").send_keys(contact.companyname)
            wd.find_element_by_name("address").click()
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys(contact.address)
            wd.find_element_by_name("theform").click()
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(contact.email)
            wd.find_element_by_name("phone2").click()
            wd.find_element_by_name("phone2").clear()
            wd.find_element_by_name("phone2").send_keys(contact.phone2)
            # submit contact creation
            wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
            # go to home page
            self.return_to_homepage()

    def open_create_contact_page(self):
            wd = self.app.wd
            wd.find_element_by_link_text("add new").click()