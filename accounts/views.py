from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages
# Create your views here.
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form =RegistrationForm(request.POST)
        if form.is_valid():
            firs_name = form.cleaned_data['firs_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            user = Account.objects.create_user(firs_name=firs_name, last_name=last_name, username=username, email=email,  password=password)
            user.phone_number = phone_number
            user.save()
            messages.success(request,'Se registro el usuario exitosamente.')
            return redirect('register')


    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return 