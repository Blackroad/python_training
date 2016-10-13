from Model.contacts import Contacts
import random
import re






class ContactHelper:
    def __init__(self,app):
        self.app = app

    def add(self, Contacts):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(Contacts)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def add_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.select_contact_by_id(contact_id)
        self.select_group_for_contact_by_id(group_id)
        wd.find_element_by_name('add').click()
        self.app.open_home_page()
        self.contact_cache = None


    def select_group_for_contact_by_id(self,id):
        wd = self.app.wd
        wd.find_element_by_xpath("//select[@name='to_group']/option[@value='%s']" %id).click()




    def fill_contact_form(self, Contacts):
        wd = self.app.wd
        self.change_field_value("firstname", Contacts.firstname)
        self.change_field_value("lastname", Contacts.lastname)
        self.change_field_value("middlename", Contacts.initials)
        self.change_field_value("nickname", Contacts.nickname)
        self.change_field_value("home", Contacts.homephone)
        self.change_field_value("email", Contacts.email)
        self.change_field_value("mobile", Contacts.mobilephone)
        self.change_field_value("work", Contacts.workphone)
        self.change_field_value("fax", Contacts.fax)
        self.change_field_value("phone2", Contacts.secondaryphone)
        self.change_field_value("email2", Contacts.email2)
        self.change_field_value("email3", Contacts.email3)
        self.change_field_value("address", Contacts.address)
        self.change_field_value("address2", Contacts.address2)



    def change_field_value(self,field_name,text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_contact_by_index(self, index, new_contacts_data):
        wd = self.app.wd
        self.select_contact_by_index(index)
        self.select_edit_by_index(index)
        self.fill_contact_form(new_contacts_data)
        wd.find_element_by_name("update").click()
        self.wait("addressbook/", "maintable")
        self.contact_cache = None

    def modify_contact_by_id(self, id, new_contacts_data):
        wd = self.app.wd
       # self.select_contact_by_index(id)
        self.select_edit_by_id(id)
        self.fill_contact_form(new_contacts_data)
        wd.find_element_by_name("update").click()
        self.wait("addressbook/", "maintable")
        self.contact_cache = None

    def wait(self, url_string, elem_name):
        wd = self.app.wd
        while (wd.current_url.endswith(url_string) and len(wd.find_elements_by_name(elem_name)) > 0):
            pass
        wd.implicitly_wait(5)
        return

    def select_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def select_contact_by_id(self,id):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='%s']" % id).click()

    def select_edit_by_index(self,index):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='maintable']/tbody/tr["+ str(index+2) +"]/td[8]/a/img").click()

    def select_edit_by_id(self,id):
        wd = self.app.wd
        wd.find_element_by_xpath('//a[@href="edit.php?id=%s"]' % id).click()


    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def del_from_group_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        wd.find_element_by_name('remove').click()
        self.app.open_home_page()
        self.contact_cache = None

    def select_group_for_contact_deletion_by_id(self,id):
        wd = self.app.wd
        wd.find_element_by_xpath("//select[@name='group']/option[@value='%s']" % id).click()

    def select_all_contacts(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//select[@name='group']/option[@value=[all]]" ).click()



    def view_contact_profile_by_index(self,index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def select_first_contact(self):
        wd = self.app.wd
        self.modify_contact_by_index(0)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.wait("addressbook/", "maintable")
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                address = cells[3].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                firstname = cells[2].text
                lastname = cells[1].text
                self.contact_cache.append(Contacts(firstname=firstname, lastname=lastname,
                                                   address = address, id=id,
                                                   all_phones_from_home_page =all_phones,
                                                   all_emails_from_home_page = all_emails))
        return list(self.contact_cache)

    def contact_info_from_edit_page(self,index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contacts(firstname= firstname, lastname= lastname, id=id, homephone= homephone,
                        mobilephone = mobilephone, workphone = workphone, secondaryphone = secondaryphone,
                        address = address, email = email, email2 = email2, email3 = email3)

    def get_contact_from_view_page(self,index):
        wd = self.app.wd
        self.view_contact_profile_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)",text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        fax =re.search("F: (.*)",text).group(1)
        secondaryphone =re.search("P: (.*)",text).group(1)
        return Contacts(id=id, homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)












