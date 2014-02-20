from django.db import models

# Create your models here.


class  Login(models.Model):
    user_id_number=models.CharField(max_length=100) #The user number serves as the number
    password=models.CharField(max_length=100)      #Password for the relevent number

    def __unicode__(self):
        return self.user_id_number




class Contacts1(models.Model):
        contact_first_name=models.CharField(max_length=200)
        contact_second_name=models.CharField(max_length=200)
        contact_number=models.BigIntegerField()
        contact_email_id=models.CharField(max_length=200)

        def __unicode__(self):
             return self.contact_first_name