#to take the input of firstname
# to take the input of surname 
# to take the input of email MAKE SURE THEY INCLUDE A VALID EMAIL ADDRESS THAT CONTAINS AN @ SIGN
# to take the input of phone number KRISHAN MAKE SURE THEY CAN PUT THE CORRECT AMOUNT OF DIGITS IN ONLY
from django import forms
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

class UserForm(forms.Form):



    firstname = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    telephone_number = forms.CharField(max_length=15)
    company_name = forms.CharField(max_length=100)
    company_street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    postcode = forms.CharField(max_length=10)
    company_number = forms.CharField(max_length=9)

    filter_choices = (
        ('retail', 'Retail'),
        ('professional services', 'Professional Services'),
        ('food & drink', 'Food & Drink'),
        ('entertainment', 'Entertainment'),
    )
    
    business_sector = forms.ChoiceField(choices = filter_choices)

    days = forms.CharField(max_length=5)
    reason_for_loan = forms.CharField(max_length=2000,widget=forms.Textarea)
    
    borrowing = forms.IntegerField(validators=[MinValueValidator(10000),MaxValueValidator(100000)])
 



##    business_sector = forms.CharField(  
##        ('retail', 'retail'),
##	('professional_services', 'professional_services'),
##	('food_&_drink', 'food_&_drink'),
##	('entertainment', 'entertainment'))
##

