from Model.contacts import Contacts
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts,args = getopt.getopt(sys.argv[1:],"n:f:",["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o=="-n":
        n=int(a)
    elif o=="-f":
        f = a


def random_string(prefix,maxlen,symbols=None,digits=None):
    if symbols != None:
        symbols = string.ascii_letters + " "*10
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    elif digits !=None:
        digits = string.digits + "-"*3
        return prefix + "".join([random.choice(digits) for i in range(random.randrange(maxlen))])
    else:
        all = string.ascii_letters + string.digits +  string.punctuation + " "*10
        return prefix + "".join([random.choice(all) for i in range(random.randrange(maxlen))])

testdata = [Contacts(firstname=random_string('name', 10), lastname=random_string('s_name', 7),
                     nickname=random_string('n_name',6,symbols=1),
                     homephone=random_string('phone', 5, digits=1),
                     workphone=random_string('w_phone',5,digits=1),
                     mobilephone=random_string('m_phone',5,digits=1),
                     fax = random_string('n_name',6,digits=1),
                     secondaryphone= random_string('s_phone',6,digits=1),
                     address= random_string('address',6),
                     address2= random_string('address2',6),
                     email= random_string('mail1@',6),
                     email2= random_string('mail2@',6),
                     email3= random_string('mail3@',6))
            for x in range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",f)



with open(file, "w") as out:
    jsonpickle.set_encoder_options("json",indent = 2)
    out.write(jsonpickle.encode(testdata))