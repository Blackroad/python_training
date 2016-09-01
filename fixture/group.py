class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, Group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(Group)
        # submit group
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def fill_group_form(self, Group):
        wd = self.app.wd
        self.change_field_value("group_name", Group.name)
        self.change_field_value("group_header", Group.header)
        self.change_field_value("group_footer", Group.footer)


    def change_field_value(self, group_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(group_name).click()
            wd.find_element_by_name(group_name).clear()
            wd.find_element_by_name(group_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        #set group on edit
        wd.find_element_by_name("edit").click()
        #modify group fields
        self.fill_group_form(new_group_data)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()


    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()