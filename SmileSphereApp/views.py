from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import Appointment, Clinic, Patient, SuperAdmin
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
    #appointment_time = request.POST['appointment_time']
    return redirect('admin_dashboard')

def reject_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.status = 3  # Assuming 3 represents 'Rejected' status
    appointment.save()
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

def clinic_register(request):
    if request.method == 'POST':
        # Process the form data
        # Save clinic, doctors, and surgeons
        pass
    else:
        print('hai')
    return render(request, 'clinic_register.html')
    
def Login_cards(request):
    return render(request, 'Login_cards.html')
def Register_cards(request):
    return render(request, 'Register_cards.html')



from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import Clinic, Doctor, Surgeon

def clinic_register(request):
    if request.method == 'POST':
        # Extract clinic details from the form
        clinic_name = request.POST.get('clinic_name')
        clinic_latitude = request.POST.get('clinic_latitude')
        clinic_longitude = request.POST.get('clinic_longitude')
        clinic_photo = request.FILES.get('clinic_photo')

        # Concatenate latitude and longitude into a location string
        clinic_location = f"{clinic_latitude}, {clinic_longitude}"

        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'clinic_registration.html')

        if len(password) < 8:
            messages.error(request, 'Password should be at least 8 characters long.')
            return render(request, 'clinic_registration.html')

        hashed_password = make_password(password)

        # Create the clinic
        clinic = Clinic(name=clinic_name, location=clinic_location, photo=clinic_photo, password=hashed_password)
        clinic.save()

        # Extract doctor details from the form
        doctor_name = request.POST.get('doctor_name')
        doctor_specialty = request.POST.get('doctor_specialty')
        doctor_available_days = request.POST.get('doctor_available_days')
        doctor_photo = request.FILES.get('doctor_photo')

        # Create the doctor
        doctor = Doctor(name=doctor_name, specialty=doctor_specialty, available_days=doctor_available_days,
                        photo=doctor_photo, clinic=clinic)
        doctor.save()

        # Extract surgeon details from the form
        surgeon_name = request.POST.get('surgeon_name')
        surgeon_specialty = request.POST.get('surgeon_specialty')
        surgeon_available_days = request.POST.get('surgeon_available_days')
        surgeon_photo = request.FILES.get('surgeon_photo')

        # Create the surgeon
        surgeon = Surgeon(name=surgeon_name, specialty=surgeon_specialty, available_days=surgeon_available_days,
                          photo=surgeon_photo, clinic=clinic)
        surgeon.save()

        messages.success(request, 'Clinic, doctor, and surgeon registration successful.')
        return redirect('clinic_login')  # Assuming there's a view for clinic login
    else:
        return render(request, 'clinic_register.html')


    
from django.shortcuts import render, redirect
from django.contrib import messages

def clinic_login(request):
    if request.method == 'POST':
        clinic_name = request.POST.get('clinic_name')
        password = request.POST.get('password')

        # Perform authentication here, check if clinic_name and password are valid
        # For example:
        if clinic_name == 'valid_name' and password == 'valid_password':
            # Successful login
            # Replace 'dashboard' with the URL name of the clinic dashboard
            return redirect('dashboard')  
        else:
            messages.error(request, 'Invalid clinic name or password.')
            return redirect('clinic_login')

    return render(request, 'clinic_login.html')



from django.shortcuts import render

def clinic_dashboard(request):
    if request.method == 'POST':
        clinic_name = request.POST.get('clinic_name')
        clinic_location = request.POST.get('clinic_location')
        clinic_latitude = request.POST.get('clinic_latitude')
        clinic_longitude = request.POST.get('clinic_longitude')
        

        # Fetch details of doctors
        doctors = []
        for i in range(1, 6):  # Assuming maximum 5 doctors can be added
            doctor_name = request.POST.get(f'doctor_name_{i}')
            if doctor_name:
                doctor_specialty = request.POST.get(f'doctor_specialty_{i}')
                doctor_available_days = request.POST.get(f'doctor_available_days_{i}')
                doctor_photo = request.FILES.get(f'doctor_photo_{i}')
                doctors.append({
                    'name': doctor_name,
                    'specialty': doctor_specialty,
                    'available_days': doctor_available_days,
                    'photo': doctor_photo
                })

        # Fetch details of surgeons
        surgeons = []
        for i in range(1, 6):  # Assuming maximum 5 surgeons can be added
            surgeon_name = request.POST.get(f'surgeon_name_{i}')
            if surgeon_name:
                surgeon_specialty = request.POST.get(f'surgeon_specialty_{i}')
                surgeon_available_days = request.POST.get(f'surgeon_available_days_{i}')
                surgeon_photo = request.FILES.get(f'surgeon_photo_{i}')
                surgeons.append({
                    'name': surgeon_name,
                    'specialty': surgeon_specialty,
                    'available_days': surgeon_available_days,
                    'photo': surgeon_photo
                })

        context = {
            'clinic_name': clinic_name,
            'clinic_location': clinic_location,
            'clinic_latitude': clinic_latitude,
            'clinic_longitude': clinic_longitude,
            'doctors': doctors,
            'surgeons': surgeons,
        }

        return render(request, 'clinic_dashboard.html', context)
    else:
        # Handle GET requests or invalid requests
        return render(request, 'clinic_dashboard.html')








