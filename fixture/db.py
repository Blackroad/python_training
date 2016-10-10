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
            cursor.execute("select id, firstname, lastname, email, email2, email3, address, work, home, phone2, mobile from addressbook where deprecated ='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, email, email2, email3, address, work, home, phone2, mobile) = row
                contact_list.append(Contacts(id=str(id), firstname= firstname, lastname=lastname,
                                             email=email, email2=email2, email3=email3,
                                             address=address,
                                             workphone=work, homephone=home,secondaryphone=phone2,
                                             mobilephone=mobile))

        finally:
            cursor.close()
        return contact_list


    def destroy(self):
        self.connection.close()