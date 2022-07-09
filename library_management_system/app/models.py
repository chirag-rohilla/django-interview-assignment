from xml.dom.minidom import CharacterData
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField as Char 
from django.db.models.fields import IntegerField as Int 
from django.db.models.fields import DateField as data
from datetime import datetime ,timedelta 


class UserExtend (models.Model):
    user = models.OneToOneField(User,default=1,on_delete=models.CASCADE)
    ph_no= Int()
    def __str__(self):
        return self.user.username

class AddBook (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = Char(max_length=10)
    book_id = Char(max_length=10)
    subject = Char(max_length=10)
    author = Char(max_length=15)
    def __str__(self):
        return str(self.book_name)+" : "+str(self.book_id)

def expiry():
    return datetime.today + timedelta(days=15)

class IssueBook (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    m_id = Char(max_length=10)
    bookid1 = Char(max_length=10)
    issuedate = data(auto_now=True)
    expirydate = data(default = expiry) 
    def __str__(self):
        return self.m_id
    
class ReturnBook (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    bookid2 = Char(max_length=10)
    
class AddMember(models.Model):
    user = models.OneToOneField(User,default=0, on_delete=models.CASCADE)
    m_name = Char(max_length=10)
    m_id = Char(max_length=10)
    def __str__(self):
        return str(self.m_name)+' : '+str(self.m_id)