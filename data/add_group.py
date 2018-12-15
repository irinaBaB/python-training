from model.group import Group
import random
import string


def random_string (prefix,maxlen):
    symbols = string.ascii_letters + string.digits +" "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata=[
    Group(name = name, header=header, footer=footer)
    for name in ["",random_string("name",10)]
    for header in ["",random_string("header",20)]
    for footer in ["", random_string("footer",15)]
    for i in range(1)
]