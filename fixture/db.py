import pymysql.cursors
from Model.group import Group
from Model.contacts import Contacts

class Dbfixture:
    def __init__(self,host,name,user,password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit(True)


    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id,group_name,group_header,group_footer from group_list")
            for row in cursor:
                (id,name,header,footer)=row
                list.append(Group(id=str(id),name=name,header=header,footer=footer) )
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook")
            for row in cursor:
                (id, firstname, lastname, nickname) = row
                contact_list.append(Contacts(id=str(id),first_name = firstname, last_name=lastname))
        finally:
            cursor.close()
        return contact_list


    def destroy(self):
        self.connection.close()