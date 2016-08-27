class ContactHelper:
    def __init__(self,app):
        self.app = app

    def add(self, Contacts):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Contacts.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Contacts.lastname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(Contacts.initials)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Contacts.nickname)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(Contacts.homephone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(Contacts.email)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def modify(self, Contacts):
        wd = self.app.wd
        #select fist contact in list
        wd.find_element_by_name("selected[]").click()
        #click 'edit' control
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        #modify contact fields
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Contacts.firstname)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Contacts.lastname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(Contacts.initials)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Contacts.nickname)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(Contacts.homephone)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(Contacts.email)
        #submit changes
        wd.find_element_by_name("update").click()

    def delete(self):
        wd = self.app.wd
        # select fist contact in list
        wd.find_element_by_name("selected[]").click()
        # click 'delete' control
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()





