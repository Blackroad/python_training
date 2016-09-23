from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contacts import ContactHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        #self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contacts = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("maintable")) > 0):
            wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False