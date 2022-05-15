from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
import random

# from .models import related models
from .models import CarModel, CarMake, CarDealer, DealerReview
# from .restapis import related methods
from .restapis import get_request, get_dealers_from_cf, get_dealer_reviews_from_cf, post_request, get_dealer_by_id_from_cf
from .restapis import get_dealers_url, get_reviews_url, post_reviews_url

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
# def about(request):
# ...
def about(request):
    context = {}
    return render(request, 'djangoapp/about.html', context)

# Create a `contact` view to return a static contact page
#def contact(request):
def contact(request):
    context = {}
    return render(request, 'djangoapp/contact.html', context)

# Create a `login_request` view to handle sign in request
# def login_request(request):
# ...
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
            return render(request, 'djangoapp/index.html', context)
    else:
        return render(request, 'djangoapp/index.html', context)

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
# ...
def logout_request(request):
    logout(request)
    return redirect('djangoapp:index')

# Create a `registration_request` view to handle sign up request
# def registration_request(request):
# ...
def registration_request(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'djangoapp/registration.html', context)
    elif request.method == 'POST':
        # Check if user exists
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.error("New user")
        if not user_exist:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            login(request, user)
            return redirect("djangoapp:index")
        else:
            context['message'] = "User already exists."
            return render(request, 'djangoapp/index.html', context)

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    # if request.method == "GET":
    #     return render(request, 'djangoapp/index.html', context)
    if request.method == "GET":
        url = get_dealers_url
        # Get dealers from the URL
        dealerships = get_dealers_from_cf(url, {})
        #print(1, dealerships[0])
        # Concat all dealer's short name
        #dealer_names = '<br>'.join([str(dealer) for dealer in dealerships])
        context['dealership_list'] = dealerships
        # Return a list of dealer short name
        #return HttpResponse(dealer_names)
        return render(request, 'djangoapp/index.html', context)
        

# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...
def get_dealer_details(request, dealerId):
    if request.method == "GET":
        context = {}
        url = get_reviews_url
        # Get dealers from the URL
        dealer_reviews = get_dealer_reviews_from_cf(url, dealerId)
        context['dealer_review_list'] = dealer_reviews
        context["dealer"] = get_dealer_by_id_from_cf(get_dealers_url, dealerId)[0]
        #print(1, dealer_reviews)
        # Concat all dealer's reviews
        #dealer_reviews_text = '<br>'.join([str(review) for review in dealer_reviews])
        # Return a list of dealer short name
        #return HttpResponse(dealer_reviews_text)
        return render(request, 'djangoapp/dealer_details.html', context)

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...
def add_review(request, dealerId):
    
    # User must be logged in before posting a review
    if request.user.is_authenticated:
        # GET request renders the page with the form for filling out a review
        if request.method == "GET":
            context = {
                "cars": CarModel.objects.all(),
                "dealer": get_dealer_by_id_from_cf(get_dealers_url, dealerId)[0],
                }
            
            return render(request, 'djangoapp/add_review.html', context)
           
        # POST request posts the content in the review submission form to the Cloudant DB using the post_review Cloud Function
        if request.method == "POST":
            form = request.POST
            #print("form", form)
            review = dict()
            review["id"] = random.randrange(150,1000,1)
            review["name"] = f"{request.user.first_name} {request.user.last_name}"
            review["dealership"] = dealerId
        
            review["review"] = form["content"]
            
            review["purchase"] = form.get("purchasecheck")
            if review["purchase"]:
                review["purchase_date"] = str(datetime.strptime(form.get("purchasedate"), "%m/%d/%Y").isoformat())
            else: 
                review["purchase_date"] = None
           
            car = CarModel.objects.get(pk=form["car"])
            
            review["car_make"] = car.car_make.name
            review["car_model"] = car.name
            review["car_year"] = car.year.isoformat()

            json_payload = {"review": review}  # Create a JSON payload that contains the review data
            
            # Performing a POST request with the review
            #print(10, json_payload)
            result = post_request(post_reviews_url, json_payload)
            #print(result)
            if int(result.status_code) == 200:
                print("Review posted successfully.")

            # After posting the review the user is redirected back to the dealer details page
            return redirect("djangoapp:dealer_details", dealerId)

    else:
        # If user isn't logged in, redirect to login page
        print("User must be authenticated before posting a review. Please log in.")
        return redirect("/djangoapp/login")

def add_review_1(request, dealerId):
    context = {}
    if request.method == "POST":
        if request.user.is_authenticated:
            review = {}
            review["time"] = datetime.utcnow().isoformat()
            review["dealership"] = 11   
            review["review"] = "This is a great car dealer"
            # self.id=id
            # self.name=name
            # self.dealership=dealership
            # self.review=review
            # self.purchase=purchase
            # self.purchase_date=purchase_date
            # self.car_make=car_make
            # self.car_model=car_model
            # self.car_year=car_year
            # self.another=another
            # self.sentiment=sentiment
            return redirect('djangoapp:index')
        else:
            context['message'] = "Please sign in"
            return render(request, 'djangoapp/index.html', context)
        url = post_reviews_url
        # Get dealers from the URL
        dealer_reviews = get_dealer_reviews_from_cf(url, dealerId)
        #print(1, dealer_reviews)
        # Concat all dealer's reviews
        dealer_reviews_text = '<br>'.join([str(review) for review in dealer_reviews])
        # Return a list of dealer short name
        return HttpResponse(dealer_reviews_text)
