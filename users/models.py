from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
alpha = RegexValidator(r'^[zA-Z]*$', 'Only alpha characters are allowed.')
numeric = RegexValidator(r'^[0-9a]*$', 'Only numeric characters are allowed.')

class User(models.Model):
    #to store user data

    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    #telephone_number =  models.CharField('telephone_number', max_length=15, validators=[MinLengthValidator(7)])
    telephone_number = models.CharField(max_length=15)
    company_name = models.CharField(max_length=100)
    company_street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postcode = models.CharField('postcode', max_length=9, validators=[MinLengthValidator(7)])
    company_number = models.CharField(max_length=8)
    #company_number = models.CharField(validators=[RegexValidator(regex='^.{8}$', message='Length has to be 8 characters', code='nomatch')])
    
    filter_choices = (
        ('retail', 'Retail'),
        ('professional services', 'Professional Services'),
        ('food & drink', 'Food & Drink'),
        ('entertainment', 'Entertainment'),
    )
    business_sector = models.CharField(max_length=100, choices=filter_choices)
    days = models.CharField(max_length=5)
    reason_for_loan = models.CharField(max_length=2000)
    borrowing = models.IntegerField(validators=[MinValueValidator(10000),MaxValueValidator(100000)])

    #business_sector = models.CharField(max_length=100)
    #business_sector = models.ChoiceField(choices = filter_choices)
    #borrowing = models.CharField(max_length=100)
    #borrowing = models.IntegerField(choices=[(i, i) for i in range(1, 1)], blank=True)
    #borrowing = models.IntegerField((validators=[MaxValueValidator(100),MinValueValidator(1)])
    #borrowing = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)])
    #if 10000 <= borrowing <= 100000:
        #borrowing = models.CharField(max_length=100)
              
    def __str__(self):
        return self.firstname

    #else:
        #print "figure must be between 10000 100000"
