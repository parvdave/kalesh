from django.shortcuts import render, redirect, get_object_or_404
from .forms import KaleshForm, KaleshiResponseForm
from django.core.mail import send_mail
from django.core.exceptions import PermissionDenied
from .models import Kaleshi
from django.contrib import messages
from django.conf import settings

def home_view(request):
    return redirect('resolve-kalesh')

def resolve_kalesh(request):
    if request.method == 'POST':
        form = KaleshForm(request.POST)
        if form.is_valid():
            # Send confirmation email
            form.save()
            messages.success(request, 'Your Kalesh has been recorded. Check your respective emails to record a response.')
            return redirect('resolve-kalesh')  # Replace with your success page/view
    else:
        form = KaleshForm()
    return render(request, 'masala/resolve_kalesh.html', {'form': form})

def kaleshi_response_view(request, kaleshi_slug):
    # Fetch the Kaleshi object using the slug
    kaleshi = get_object_or_404(Kaleshi, kaleshi_slug=kaleshi_slug)

    if kaleshi.kaleshi_response:
        raise PermissionDenied("You are not allowed to access this page.")
    # If the request is a POST, handle the form submission
    if request.method == "POST":
        form = KaleshiResponseForm(request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Save the response to the Kaleshi object
            kaleshi.kaleshi_response = form.cleaned_data['kaleshi_response']
            kaleshi.save()  # Save the updated Kaleshi object
            
            # Redirect to a success page (or the same page after saving)
            return redirect('resolve-kalesh')
    else:
        # If it's a GET request, create an empty form
        form = KaleshiResponseForm()

    # Render the template with the form
    return render(request, 'masala/kaleshi_response.html', {'form': form, 'kaleshi': kaleshi})
