from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessonHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
#from selenium.webdriver.chrome.webdriver import WebDriver


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessonHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()


