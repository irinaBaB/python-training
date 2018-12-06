from sys import maxsize

class Contact:

     def __init__(self, firstname=None,middlename=None,lastname=None,nickname=None, companyname=None,address=None,email=None,phone2=None,mobile=None,id= None):
            self.firstname = firstname
            self.middlename = middlename
            self.lastname = lastname
            self.nickname = nickname
            self.companyname = companyname
            self.address = address
            self.email = email
            self.phone2 = phone2
            self.mobile = mobile
            self.id = id


     def __repr__(self):
         return '%s.%s' % (self.id, self.lastname)

     def __eq__(self, other):
         return (self.id is None or other.id is None or self.id == other.id or self.lastname == other.lastname)\
                or self.firstname == other.firstname

     def id_or_max(self):
         if self.id:
             return int(self.id)
         else:
             return maxsize


