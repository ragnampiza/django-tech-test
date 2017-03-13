from django.shortcuts import render
from users.forms import UserForm
from users.models import User

# the function executes with the signup url to take the inputs 
def signup(request):
    if request.method == 'POST':  # if the form has been filled

        form = UserForm(request.POST)
        if form.is_valid():
            # Form is valid. Because the Form (ModelForm) is bound to the User model, then it will create, save in db and return the instance automatically.
            user_obj = form.save()
            return render(request, 'users/signup.html', {'user_obj': user_obj,'is_registered':True })  # Redirect after POST


            form = UserForm(request.POST)
            # creating user data
            firstname = request.POST.get('firstname', '')
            surname = request.POST.get('surname', '')
            email = request.POST.get('email', '')
            telephone_number = request.POST.get('telephone_number', '')
            company_name = request.POST.get('company_name', '')
            company_street_address = request.POST.get('company_street_address', '')
            city = request.POST.get('city', '') 
            postcode = request.POST.get('postcode', '') 
            company_number = request.POST.get('company_number', '')
            form = request.POST.get('form', '')
            business_sector = request.POST.get('business_sector', '')
            borrowing = request.POST.get('borrowing', '')        
            days = request.POST.get('days', '')
            reason_for_loan = request.POST.get('reason_for_loan', '')

            user_obj = User(firstname=firstname, surname=surname, email=email,
            telephone_number=telephone_number,company_name=company_name,
                    company_street_address=company_street_address,city=city,
                    postcode=postcode,company_number=company_number,
                    business_sector=business_sector,borrowing=borrowing,
                    days=days,reason_for_loan=reason_for_loan)

            user_obj.save()        
            return render(request, 'users/signup.html', {'user_obj': user_obj,'is_registered':True })  # Redirect after POST
            
        # saving all the data in the current object into the database
    else:
        form = UserForm()  # an unboundform
        return render(request, 'users/signup.html', {'form': form})

#the function executes with the showdata url to display the list of registered users
def showdata(request):
    all_users = User.objects.all()
    return render(request, 'users/showdata.html', {'all_users': all_users, })
