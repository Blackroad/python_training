from sys import maxsize


class Contacts:

    def __init__(self, first_name = None, last_name = None, initials = None, nickname = None, home_phone = None, email = None,
                 id = None, mobilephone = None, fax = None, workphone = None, secondaryphone = None ):
        self.firstname = first_name
        self.lastname = last_name
        self.initials = initials
        self.nickname = nickname
        self.homephone = home_phone
        self.mobilephone = mobilephone
        self.fax = fax
        self.secondaryphone = secondaryphone
        self.workphone = workphone
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname,self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize