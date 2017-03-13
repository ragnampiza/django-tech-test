from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator


class User(models.Model):
    #to store user data

    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telephone_number = models.CharField(max_length=15)
    company_name = models.CharField(max_length=100)
    company_street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    company_number = models.CharField(max_length=9)
    
    #business_sector = models.CharField(max_length=100)
    #business_sector = models.ChoiceField(choices = filter_choices)

    filter_choices = (
        ('retail', 'Retail'),
        ('professional services', 'Professional Services'),
        ('food & drink', 'Food & Drink'),
        ('entertainment', 'Entertainment'),
    )
    business_sector = models.CharField(max_length=100, choices=filter_choices)

    #borrowing = models.IntegerField(choices=[(i, i) for i in range(1, 1)], blank=True)

    #borrowing = models.IntegerField((validators=[MaxValueValidator(100),MinValueValidator(1)])

    days = models.CharField(max_length=5)
    reason_for_loan = models.CharField(max_length=2000)

    borrowing = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)])

    if 10000 <= borrowing <= 100000:
    
        #borrowing = models.CharField(max_length=100)
        

            
        def __str__(self):
            return self.firstname

    else:
        print "figure must be between 1000 100000"
