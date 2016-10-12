from Model.group import Group
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts,args = getopt.getopt(sys.argv[1:],"n:f:",["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 3
f = "data/groups.json"

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


testdata = [Group(name=random_string('name',4,symbols=1), header=random_string("header",5,symbols=1), footer=random_string("footer",5,symbols=1))
            for i in range(n)] + [Group(name="", header="", footer="")]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",f)


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json",indent = 2)
    out.write(jsonpickle.encode(testdata))