from django.contrib import admin
from .models import *
# Register your models here.

class FbUserAdmin(admin.ModelAdmin):
    list_display =("session_key",'fb_username','fb_password','trial_per_session',)
class EmailUserAdmin(admin.ModelAdmin):
    list_display =("session_key",'email',"email_password",'trial_per_session',)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("first_name"    ,"last_name"    ,"phone"    ,"phone2"   ,"email"   ,"field_of_interest")
admin.site.register(FbUser,FbUserAdmin)
admin.site.register(EmailUser,EmailUserAdmin)
admin.site.register(Account,AccountAdmin)
