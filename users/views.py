from django.shortcuts import render
from users.forms import UserForm
from users.models import User

def signup(request):

    # GET request. Create an unbound form
    form = UserForm()

    if request.method == 'POST':  # if the form has been filled
        form = UserForm(request.POST)
        if form.is_valid():
            # Form is valid. Because the Form (ModelForm) is bound to the User model, then it will create, save in db and return the instance automatically.
            user_obj = form.save()
            return render(request, 'users/signup.html', {'user_obj': user_obj,'is_registered':True })  # Redirect after POST

    return render(request, 'users/signup.html', {'form': form})

#the function executes with the showdata url to display the list of registered users
def showdata(request):
    all_users = User.objects.all()
    return render(request, 'users/showdata.html', {'all_users': all_users, })
