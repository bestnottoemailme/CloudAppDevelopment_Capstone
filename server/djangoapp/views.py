from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import get_dealer_by_id, get_dealers_from_cf, get_dealers_by_state, get_dealer_reviews_from_cf, post_request
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
# View to render the index page with a list of dealerships
def get_dealerships(request):
    return render(request,'djangoapp/index.html')
    # if request.method == "GET":
    #     context = {}
    #     # url = "https://9bebcb01.eu-de.apigw.appdomain.cloud/api/dealership"
    #     # # Get dealers from the Cloudant DB
    #     # context["dealerships"] = get_dealers_from_cf(url)
    #     context["dealerships"] = {}

    #     # dealer_names = ' '.join([dealer.short_name for dealer in context["dealerships"]])
    #     # return HttpResponse(dealer_names)

    #     return render(request, 'djangoapp/index.html', context)


# Create an `about` view to render a static about page
def about(request):
    return render(request,'djangoapp/about.html')


# Create a `contact` view to return a static contact page
def contact(request):
    return render(request,'djangoapp/contact.html')

# Create a `login_request` view to handle sign in request
def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('djangoapp:index')
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'djangoapp/login.html', context)
    else:
        return render(request, 'djangoapp/login.html', context)

# ...

# View to handle sign out request
def logout_request(request):
    # Get the user object based on session id in request
    print("Logging out `{}`...".format(request.user.username))
    # Logout user in the request
    logout(request)
    # Redirect user back to course list view
    return redirect('djangoapp:index')

# Create a `registration_request` view to handle sign up request
def registration_request(request):
    return render(request,'djangoapp/registration.html')




# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request, dealer_id):
    return HttpResponse(dealer_id)


# Create a `add_review` view to submit a review
def add_review(request, dealer_id):
    pass
