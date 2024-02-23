from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import Appointment, Patient, SuperAdmin
from django.shortcuts import render
from django.core.paginator import Paginator
import random
import string
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout






CustomUserCreationForm = UserCreationForm

# Define additional form fields or customizations here if needed

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')

# Common Views
def index(request):
    # Your index view logic here
    return render(request, 'index.html')
def index2(request):
    # Your index view logic here
    return render(request, 'index2.html')

@login_required
def new_appointment(request):
    return render(request, 'patient_appointment.html')


def patient_register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'patient_register.html')

        # Check if email already exists
        if Patient.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'patient_register.html')

        # If everything is fine, create the patient
        hashed_password = make_password(password)
        patient = Patient(email=email, password=hashed_password)
        patient.save()

        messages.success(request, 'Registration successful. Please log in.')
        return redirect('patient_login')
    else:
        return render(request, 'patient_register.html')

def patient_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            patient = Patient.objects.get(email=email)
        except Patient.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'patient_login.html')

        if check_password(password, patient.password):
            request.session['patient_id'] = patient.id
            # Login successful, redirect to dashboard or wherever needed
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'patient_login.html')
    else:
        return render(request, 'patient_login.html')
    

def dashboard(request):
    # Retrieve appointments for the specific user
    patient_id = request.session.get('patient_id')
    appointments = Appointment.objects.filter(patient_id=patient_id)

    # Filter by date if provided
    date_filter = request.GET.get('date')
    if date_filter:
        appointments = appointments.filter(date=date_filter)

    # Filter by status if provided
    status_filter = request.GET.get('status')
    if status_filter:
        appointments = appointments.filter(status=status_filter)

    appointments = appointments.order_by('-id')

    # Pagination
    paginator = Paginator(appointments, 3)  # Show 10 appointments per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'paginator': paginator}

    # If no appointments found, display a message
    if not appointments:
        context['no_appointments'] = True

    return render(request, 'patient_dashboard.html', context)

def patient_appointment(request):
    if request.method == 'POST':
        # Get appointment details from the form
        date = request.POST.get('date')
        description = request.POST.get('description')

        patient_id = request.session.get('patient_id')
        try:
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            messages.error(request, 'Patient does not exist.')
            return redirect('login')

        # Generate token using user's email ID and random characters
    
        random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        patient_token = f"{patient_id}-{random_chars}"

        # Create the new appointment
        appointment = Appointment(date=date, description=description, patient=patient, status=1, patient_token=patient_token)
        appointment.save()

        messages.success(request, 'Appointment created successfully.')
        return redirect('dashboard')
    else:
        return render(request, 'patient_appointment.html')
    
def admin_register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'admin-register.html')

        # Check if email already exists
        if SuperAdmin.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'admin-register.html')

        # If everything is fine, create the super admin
        hashed_password = make_password(password)
        super_admin = SuperAdmin(email=email, password=hashed_password)
        super_admin.save()

        messages.success(request, 'Registration successful. Please log in.')
        return redirect('admin-login')
    else:
        return render(request, 'admin-register.html')

def admin_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            super_admin = SuperAdmin.objects.get(email=email)
        except SuperAdmin.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'admin_login.html')

        if check_password(password, super_admin.password):
            request.session['super_admin_id'] = super_admin.id
            # Login successful, redirect to dashboard or wherever needed
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'admin_login.html')
    else:
        return render(request, 'admin_login.html')
    
def admin_dashboard(request):
        # Check if admin is logged in
    if 'super_admin_id' not in request.session:
        return redirect('admin_login')
    
    appointments = Appointment.objects.all()

    # Filter by date if provided
    date_filter = request.GET.get('date')
    if date_filter:
        appointments = appointments.filter(date=date_filter)

    # Filter by status if provided
    status_filter = request.GET.get('status')
    if status_filter:
        appointments = appointments.filter(status=status_filter)

    appointments = appointments.order_by('-id')

    # Fetching the email of the user associated with each appointment and attaching it to the appointment object
    for appointment in appointments:
        appointment.user_email = appointment.patient.email

    # Pagination
    paginator = Paginator(appointments, 3)  # Show 10 appointments per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'paginator': paginator,
    }

    # If no appointments found, display a message
    if not appointments:
        context['no_appointments'] = True

    return render(request, 'admin_dashboard.html', context)





def accept_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.status = 2  # Assuming 2 represents 'Accepted' status
    appointment.save()
    return redirect('admin_dashboard')

def reject_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.status = 3  # Assuming 3 represents 'Rejected' status
    appointment.save()
    appointment_time = request.POST['appointment_time']
    return redirect('admin_dashboard')



def reset_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('reset_password')

        # Retrieve the patient object
        patient_id = request.session.get('patient_id')
        patient = Patient.objects.get(pk=patient_id)

        # Update the patient's password
        patient.password = make_password(new_password)
        patient.save()

        messages.success(request, "Password updated successfully.")
        return redirect('dashboard')  # Redirect to the patient dashboard or any other desired page

    return render(request, 'reset_password.html')



