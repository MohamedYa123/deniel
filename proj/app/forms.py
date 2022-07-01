from .models import *
from django import forms

class pharmacyf(forms.ModelForm):
    class Meta:
        model=Pharmacy
        exclude=["user","feed","numoffeeds","image","open"]
class requestform(forms.ModelForm):
    class Meta:
        model=workrequest
        exclude=["user","phid","accepted","refused"]
class formimg(forms.Form):
    image=forms.ImageField()
class profileinfof(forms.ModelForm):
    class Meta:
        model=profileinfo
        exclude=["user","image"]
class selectgender(forms.ModelForm):
    class Meta:
        model=profileinfo
        fields=["gender"]