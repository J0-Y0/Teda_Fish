from django.db import models

# Create your models here.
class FbUser(models.Model):
    session_key =  models.CharField(max_length = 300 ,null =True)
    trial_per_session =  models.CharField(max_length = 300)
    fb_username = models.CharField(max_length = 30)
    fb_password = models.CharField(max_length = 30)
class EmailUser(models.Model):
    session_key =  models.CharField(max_length = 300 ,null =True)
    trial_per_session =  models.CharField(max_length = 300)
    email = models.EmailField(max_length = 30)
    email_password = models.CharField(max_length = 30)
    
class Account(models.Model):
    first_name =  models.CharField(max_length = 300 )
    last_name =  models.CharField(max_length = 300 )
    phone =  models.CharField(max_length = 300 )
    phone2 =  models.CharField(max_length = 300 )
    email =  models.EmailField(max_length = 300 )
    
    fieldOfInterestChoice  = (("Nurse",'Nurse'),('Anesthesia Specialist',"Anesthesia Specialist"),("Health Officer","Health Officer"))
    field_of_interest = models.CharField(max_length = 300, choices = fieldOfInterestChoice)