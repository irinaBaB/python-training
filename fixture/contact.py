from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def return_to_homepage(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")and
                len(wd.find_elements_by_xpath("//*[@id='content']/form[2]/div[1]/input"))>0):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        # create contact
        wd = self.app.wd
        # open contact page
        self.open_create_contact_page()
        self.fill_out_createcontact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//*[@id='content']/form/input[21])").click()
        # go to home page
        self.return_to_homepage()
        self.contact_cache = None

    def fill_out_createcontact_form(self, contact):
        wd = self.app.wd
        self.change_field_contact_value("firstname", contact.firstname)
        self.change_field_contact_value("middlename", contact.middlename)
        self.change_field_contact_value("lastname", contact.lastname)
        self.change_field_contact_value("nickname", contact.nickname)
        self.change_field_contact_value("company", contact.companyname)
        self.change_field_contact_value("address", contact.address)
        self.change_field_contact_value("email", contact.email)
        self.change_field_contact_value("phone2", contact.phone2)
        self.change_field_contact_value("mobile",contact.mobile)

    def change_field_contact_value(self,field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_contact(self):
        wd = self.app.wd
        self.modify_group_by_index(0)

    def modify_group_by_index(self,index, new_contact_data):
        wd = self.app.wd
        self.return_to_homepage()
        self.select_contact_by_index(index)
        # click to edit link
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # update required fields
        self.fill_out_createcontact_form(new_contact_data)
        # click to update contact form
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_homepage()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self,index):
        wd = self.app.wd
        self.return_to_homepage()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        #wd.implicitly_wait(50)
        alert = wd.switch_to.alert
        alert.accept()
        self.return_to_homepage()
        self.contact_cache = None

    def open_create_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def count(self):
        wd = self.app.wd
        self.return_to_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache= None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_homepage()
            self.contact_cache=[]
            for element in wd.find_elements_by_css_selector("td:nth-child(2)"):
                # wd.implicitly_wait(50)
                text = element.text
            for element in wd.find_elements_by_css_selector("td:nth-child(3)"):
                text2 = element.text
            for element in wd.find_elements_by_css_selector("td:nth-child(1)"):
                # wd.implicitly_wait(50)
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname=text,firstname=text2,id=id))
        return list (self.contact_cache)






















































