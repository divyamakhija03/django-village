from django.db import models

# Create your models here.
class grievanceForm(models.Model):
    first_name=models.CharField(max_length=70)
    last_name=models.CharField(max_length=70)
    email=models.CharField(max_length=500)
    aadhar_card=models.CharField(max_length=12)
    address=models.CharField(max_length=1000)
    issue=models.CharField(max_length=1000)
    city=models.CharField(max_length=100)
    pincode=models.CharField(max_length=20)
    date=models.DateTimeField(auto_now_add=True,null=False)


 
