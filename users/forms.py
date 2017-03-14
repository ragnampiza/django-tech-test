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
    #borrowing = forms.IntegerField(validators=[MinValueValidator(10000),MaxValueValidator(100000)])

# borrowing limit validation

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_borrowing(self):
       borrowing = self.cleaned_data['borrowing']
       if not 10000 <= borrowing <= 100000:
           raise forms.ValidationError("Please enter a borrowing value between 10000 and 100000")
       return borrowing

# company number length validation
    
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_company_number(self):
       company_number = self.cleaned_data['company_number']
       if not 6 <= len(company_number) <= 8:
           raise forms.ValidationError("Company number must be 8 digits long")
       return company_number

# email address validation using @ sign

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_email(self):
       email = self.cleaned_data['email']
       if '@' not in email:
           raise forms.ValidationError("Must be a valid email address")
       return email

# telephone number length confirmation

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_telephone_number(self):
       telephone_number = self.cleaned_data['telephone_number']
       if not 6 <= len(telephone_number) <= 14:
           raise forms.ValidationError("Must be a valid telephone number")
       return telephone_number

# postcode length confirmation    

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_postcode(self):
       postcode = self.cleaned_data['postcode']
       if not 6 <= len(postcode) <= 8:
           raise forms.ValidationError("Must be a valid postcode")
       return postcode


    

