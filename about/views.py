from django.shortcuts import render, get_object_or_404
from .models import Enquiry
from django.contrib import messages
from .forms import EnquiryForm
# from django.core.mail import send_mail
# import os
# if os.path.isfile('env.py'):
#     import env


def display_contact(request):
    """
    Displays the Contact page
    Validates contact form and saves
    Sends email of contact form
    """
    # SEND_MAIL_EMAIL = os.environ.get('SEND_MAIL_EMAIL')

    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            print('form was valid')
            form.save()
            messages.success(request, ('Your message has been sent!'))

            # Send enquiry form as email
            # send_mail(
            #     'C3DS Website Enquiry from ' + form.cleaned_data['full_name'],
            #     form.cleaned_data['message'],
            #     form.cleaned_data['email'],
            #     [SEND_MAIL_EMAIL],
            # )

    form = EnquiryForm()
    return render(
        request, 'contact.html', {'form': form})


def display_about(request):
    """
    Displays the about page
    """
    return render(request, 'about.html', {})


def display_partners(request):
    """
    Displays the partners page
    """
    return render(request, 'partners.html', {})
