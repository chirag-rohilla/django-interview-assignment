from django.contrib import admin
#from django.contrib.sessions.models import Session
from .models import AddBook, AddMember, IssueBook, ReturnBook, UserExtend

# Register your models here.

#admin.sites.register(UserExtend)

admin.site.register(UserExtend)

class AddBook_admin(admin.ModelAdmin):
    list_display = ("user","book_name", "book_id", "subject" , "author")
admin.site.register(AddBook,AddBook_admin)

class IssueBook_admin(admin.ModelAdmin):
    list_display = ("user", "m_id", "bookid1", "issuedate", "expirydate")
admin.site.register(IssueBook,IssueBook_admin)

class ReturnBook_admin(admin.ModelAdmin):
    list_display =("user", "bookid2")
admin.site.register(ReturnBook, ReturnBook_admin)

class AddMember_admin(admin.ModelAdmin):
    list_display = ("user", "m_name", "m_id")
admin.site.register(AddMember,AddMember_admin)
