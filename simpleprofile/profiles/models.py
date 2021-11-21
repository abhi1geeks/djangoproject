
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .validators import validator_password,validator_mobileNumber,validator_dob
# Create your models here.

class SimpleProfiles(models.Model):
    # (firstName,lastName,dob,email,mobileNumber,password)
    firstName = models.CharField(max_length=200, null=False,blank=False,help_text=_('*'))
    lastName = models.CharField(max_length=200, null=True)
    dob= models.DateField(null=False,blank=False,validators=[validator_dob],
    help_text=_('*It should be in DD-MM-YYYY format.'))
    email= models.EmailField(null=False,unique=True,blank=False,help_text=_('*'))
    mobileNumber=models.CharField(blank=False,unique=True,validators=[validator_mobileNumber],max_length=13,
    help_text=_('*It should be indian mobile number.'))
    password = models.CharField(max_length=200,null=False,unique=False,validators=[validator_password],
    help_text=_('*Password should contai: number, special character, alphabate(upeer and lower).'))

    def __str__(self) -> str:
        return self.firstName + " "+ self.lastName