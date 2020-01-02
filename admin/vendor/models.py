from django.db import models

# Create your models here.

class Vendor(models.Model): 
    
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=50)
    is_email_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)     
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'vendor'

    
   
        
    