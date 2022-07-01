from django.db import models
from django.conf import settings

from decimal import Decimal
# Create your models here.
class genders(models.Model):
    text=models.CharField(max_length=100)
    def __str__(self):
        return self.text
class government(models.Model):
    text=models.CharField(max_length=100)
    def __str__(self):
        return self.text
class Pharmacy(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    description=models.TextField()
    feed=models.DecimalField(max_digits=5,decimal_places=1,default=Decimal(3.0),null=True,blank=True)
    numoffeeds=models.DecimalField(max_digits=10**9,decimal_places=1,default=Decimal(0.0),null=True,blank=True)
    image = models.ImageField(default="")
    location=models.ForeignKey(government,on_delete=models.CASCADE,default=0)
    info_for_accepted_requests=models.TextField(default='')
    open=models.BooleanField(default=True)
    def __str__(self):
        return self.Title
class feedback(models.Model):
    phid=models.ForeignKey(Pharmacy,on_delete=models.CASCADE)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    value=models.DecimalField(max_digits=5,decimal_places=1,default=Decimal(3.0),null=True,blank=True)
    Comment=models.TextField()
class worker(models.Model):
    name=models.CharField(default="worker",max_length=100)#worker , manager , pharmacist
    def __str__(self):
        return self.name
class shift(models.Model):
    name=models.CharField(default="morning",max_length=100)#morning , afternoon , evening
    def __str__(self):
        return self.name
class workrequest(models.Model):
    phid=models.ForeignKey(Pharmacy,on_delete=models.CASCADE)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    workertype=models.ForeignKey(worker,on_delete=models.CASCADE)
    shifttype=models.ForeignKey(shift,on_delete=models.CASCADE)
    requesttext = models.TextField()
    accepted=models.BooleanField(default=False)
    refused=models.BooleanField(default=False)
    def __str__(self):
        return "request from \'user\' "+"as "+str(self.workertype) +" shift "+str(self.shifttype)
class profileinfo(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    First_name=models.CharField(default="",max_length=100)
    Last_name=models.CharField(default="",max_length=100)
    About = models.TextField(default="")
    image=models.ImageField(default="user.png")
    location = models.ForeignKey(government, on_delete=models.CASCADE,default=1)
    gender = models.ForeignKey(genders, on_delete=models.CASCADE,default=1)
    Age=models.IntegerField(default=18)
class file(models.Model):
    myfile=models.FileField(default="")



