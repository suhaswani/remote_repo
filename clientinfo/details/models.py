from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField


class ClientDetails(models.Model):
    first_Name = models.CharField(max_length=150)
    last_Name = models.CharField(max_length=150)
    phone = PhoneNumberField(region='IN')
    clientValue_USD = MoneyField(max_digits=14,decimal_places=2,default_currency='USD')
    email = models.EmailField()
    website = models.URLField()
    address = models.CharField(max_length=150)


    def __str__(self):
         return self.first_Name


    class Meta:
        db_table = 'ClientDetails'



