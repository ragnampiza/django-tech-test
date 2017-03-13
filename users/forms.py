from django import forms
from django.core.validators import ValidationError
from .models import User
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.core.validators import RegexValidator
from .models import User

class UserForm(forms.Form):

    firstname = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    telephone_number = forms.CharField(max_length=15)
    company_name = forms.CharField(max_length=100)
    company_street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    postcode = forms.CharField(max_length=10)
    #company_number = forms.CharField(validators=[RegexValidator(regex='^.{8}$', message='Length has to be 8 characters', code='nomatch')])
    company_number = forms.CharField(max_length=8)
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

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_borrowing(self):
       borrowing = self.cleaned_data['borrowing']
       if not 10000 < borrowing < 100000:
           raise forms.ValidationError("Your error message here")
       return borrowing
    
    #'borrowing = forms.CharField(max_length=9)
    #borrowing = forms.IntegerField(validators=[MinValueValidator(10000),MaxValueValidator(100000)])

##    def clean_borrowing(self):
##        borrowing = self.cleaned_data['borrowing']
##        if not 10000 < borrowing < 100000:
##            raise forms.ValidationError("Please enter a borrowing value between " \
##                                    "10000 and 100000")
##
##        return borrowing
##
##
##    borrowing = cleaned_data['borrowing']
##    if not 10000 < borrowing < 100000:
##        raise forms.ValidationError("Please enter a borrowing value between 10000 and 100000")
##    else:
##        borrowing = cleaned_data['borrowing']
## 



##    business_sector = forms.CharField(  
##        ('retail', 'retail'),
##	('professional_services', 'professional_services'),
##	('food_&_drink', 'food_&_drink'),
##	('entertainment', 'entertainment'))
##

