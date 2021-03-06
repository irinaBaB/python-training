from sys import maxsize

class Contact:

     def __init__(self, firstname=None,
                  middlename=None,
                  lastname=None,
                  nickname=None,
                  companyname=None,
                  address=None,
                  email=None,
                  home=None,
                  work=None,
                  mobile=None,
                  phone2=None,
                  fax=None,
                  id= None,
                  email2=None,
                  email3=None,
                  all_emails_from_home_page=None,
                  all_phones_from_home_page = None):
            self.firstname = firstname
            self.middlename = middlename
            self.lastname = lastname
            self.nickname = nickname
            self.companyname = companyname
            self.address = address
            self.email = email
            self.home = home
            self.fax = fax
            self.work = work
            self.mobile = mobile
            self.phone2= phone2
            self.id = id
            self.email2=email2
            self.email3 = email3
            self.all_emails_from_home_page=all_emails_from_home_page
            self.all_phones_from_home_page = all_phones_from_home_page


     def __repr__(self):
         return '%s.%s.%s.%s' % (self.id, self.lastname,self.firstname,self.email)

     def __eq__(self, other):
         return (self.id is None or other.id is None or self.id == other.id or self.lastname == other.lastname)\
                or self.firstname == other.firstname

     def id_or_max(self):
         if self.id:
             return int(self.id)
         else:
             return maxsize




