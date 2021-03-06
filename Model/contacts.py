from sys import maxsize


class Contacts:

    def __init__(self, firstname = None, lastname = None, initials = None, nickname = None, homephone = None, email = None,
                 id = None, mobilephone = None, fax = None, workphone = None, secondaryphone = None,
                 email2 = None, email3 = None, address = None, address2= None,
                 all_emails_from_home_page = None, all_phones_from_home_page = None):
        self.firstname = firstname
        self.lastname = lastname
        self.initials = initials
        self.nickname = nickname
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.fax = fax
        self.secondaryphone = secondaryphone
        self.workphone = workphone
        self.email = email
        self.email2= email2
        self.email3 = email3
        self.id = id
        self.address = address
        self.address2 = address2
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page


    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s%s:%s:%s:%s%s" % (self.id, self.firstname,self.lastname,
                                   self.address,self.email,self.email2,self.email3, self.workphone,self.secondaryphone,
                                                 self.homephone,self.mobilephone)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize