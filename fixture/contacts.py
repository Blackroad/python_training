class ContactHelper:
    def __init__(self,app):
        self.app = app

    def add(self, Contacts):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(Contacts)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_contact_form(self, Contacts):
        wd = self.app.wd
        self.change_field_value("firstname", Contacts.firstname)
        self.change_field_value("lastname", Contacts.lastname)
        self.change_field_value("middlename", Contacts.initials)
        self.change_field_value("nickname", Contacts.nickname)
        self.change_field_value("home", Contacts.homephone)
        self.change_field_value("email", Contacts.email)

    def change_field_value(self,field_name,text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify(self, new_contacts_data):
        wd = self.app.wd
        #select fist contact in list
        self.select_first_contact()
        #click 'edit' control
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        #modify contact fields
        self.fill_contact_form(new_contacts_data)
        #submit changes
        wd.find_element_by_name("update").click()

    def wait(self, url_string, elem_name):
        wd = self.app.wd
        if not (wd.current_url.endswith(url_string) and len(wd.find_elements_by_name(elem_name)) > 0):
            wd.implicitly_wait(5)
        return

    def select_first_contact(self):
        wd = self.app.wd
        self.wait("addressbook/","maintable")
        wd.find_element_by_name("selected[]").click()

    def delete(self):
        wd = self.app.wd
        # select fist contact in list
        self.select_first_contact()
        # click 'delete' control
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))









