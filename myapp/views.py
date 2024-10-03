# your_app/views.py
from django.shortcuts import render, redirect
from .models import UserRegistration
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
# Index
def home_view(request):
    return render(request, 'home.html')


def login_view(request):
    return render(request, 'login.html')

def header_view(request):
    return render(request, 'header.html')

def contact_view(request):
    return render(request, 'contact.html')

def about_view(request):
    return render(request, 'about.html')

def register_view(request):
    if request.method == 'POST':
        # Create a UserRegistration instance
        user = UserRegistration(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            middle_name=request.POST.get('middle_name', ''),
            sex=request.POST['sex'],
            dob=request.POST['dob'],
            region_code=request.POST['region_code'],
            province_code=request.POST['province_code'],
            city_municipality_code=request.POST['city_municipality_code'],
            barangay_code=request.POST['barangay_code'],
            house_number=request.POST['house_number'],
            password=request.POST['password'],  # Remember to hash this in production!
            user_type=request.POST['user_type'],
            phone_number=request.POST['phone_number'],
            email=request.POST['email'],
            valid_id=request.FILES['valid_id'],
            documents=request.FILES['documents'],
            terms_conditions='terms_conditions' in request.POST,  # Converts to True if checked
            data_privacy='data_privacy' in request.POST,
        )

        # Save the user registration
        user.save()
        messages.success(request, 'Registration successful!')
        return redirect('home_url')  # Redirect to a success page or home

    return render(request, 'register.html')  # Render the registration form

