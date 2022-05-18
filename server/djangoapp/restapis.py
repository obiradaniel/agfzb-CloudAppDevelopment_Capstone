import requests
import json
# import related models here
from requests.auth import HTTPBasicAuth
from .models import CarModel, CarMake, CarDealer, DealerReview
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, SentimentOptions
from datetime import datetime
import sys
from cloudant.client import Cloudant
from cloudant.error import CloudantException

get_dealers_url = "https://f3f2bfb2.us-south.apigw.appdomain.cloud/capstone/dealership"

get_reviews_url = "https://f3f2bfb2.us-south.apigw.appdomain.cloud/capstone/review"

post_reviews_url = "https://f3f2bfb2.us-south.apigw.appdomain.cloud/capstone/postreview"

watson_api_key = 'V4DcprQ0eFHozpjna5J8_SCpC3ESwaG01Yx42ckiZjdx'

watson_service_url = 'https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/d903d5d8-7577-402a-82d7-7e640b727f92'


authenticator = IAMAuthenticator(watson_api_key)
natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2022-04-07',
        authenticator=authenticator)
natural_language_understanding.set_service_url(watson_service_url)

# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))
def get_request(url, kwargs, api_key=None):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        # Call get method of requests library with URL and parameters
        if api_key:
            response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs, auth=HTTPBasicAuth('apikey', api_key))
            status_code = response.status_code
            print("With status {} ".format(status_code))
            json_data = json.loads(response.text)
            return json_data
        else:
            response = requests.get(url, headers={'Content-Type': 'application/json'},
                                        params=kwargs)
            status_code = response.status_code
            print("With status {} ".format(status_code))
            json_data = json.loads(response.text)
        return json_data
    except:
        # If any error occurs
        print("Network exception occurred")

#k=get_request(get_dealers_url, {"state":"CA"})
#k=get_request(get_reviews_url, {"dealerId":5})

# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)


# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list
def get_dealers_from_cf(url, kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url, kwargs)['body']
    #print("json", json_result)
    if json_result:
        # Get the row list in JSON as dealers
        if "rows" in json_result:
            dealers = json_result["rows"]
            for dealer in dealers:
                # Get its content in `doc` object
                dealer_doc = dealer["doc"]
                if "address" in dealer_doc:
                    # Create a CarDealer object with values in `doc` object
                    #print(1, dealer_doc)
                    #all_reviews=get_request(get_reviews_url, {"dealerId":dealer_doc["id"]})
                    #no_reviews = len(all_reviews['body']['data']['docs'])
                    dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                        id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                        short_name=dealer_doc["short_name"], state = dealer_doc["state"],
                                        st=dealer_doc["st"], zip=dealer_doc["zip"], totalreviews=dealer_doc["review_count"])
                    results.append(dealer_obj)
        else:
            dealers = json_result["docs"]
            for dealer in dealers:
                # Get its content in `doc` object
                dealer_doc = dealer
                #print(2, dealer_doc)
                if "address" in dealer_doc:
                    # Create a CarDealer object with values in `doc` object
                    dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                        id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                        short_name=dealer_doc["short_name"], state = dealer_doc["state"],
                                        st=dealer_doc["st"], zip=dealer_doc["zip"], totalreviews=dealer_doc["review_count"])
                    results.append(dealer_obj)
        # For each dealer object
        
    return results

def get_dealer_by_id_from_cf(url, dealerId):
    return get_dealers_from_cf(url, {"id":dealerId})

def get_dealer_by_state_from_cf(url, state):
    return get_dealers_from_cf(url, {"state":state})

# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative

def analyze_review_sentiments(text):
    text = text + "hello hello hello"
    response = natural_language_understanding.analyze( text=text,
    features=Features(sentiment=SentimentOptions(targets=[text]))).get_result()
    label=json.dumps(response, indent=2)
    label = response['sentiment']['document']['label']
    
    return label

# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list

def get_dealer_reviews_from_cf(url, dealerId):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url, {"dealerId":dealerId})['body']['data']
    #print("json_result\n", json_result, "\n")
    if json_result:
        # Get the row list in JSON as dealers
        if "docs" in json_result:
            if json_result["docs"] == []:
                return []
            else:
                reviews = json_result["docs"]
                for review in reviews:
                    # Get its content in `doc` object
                    review_doc = review
                    #print(2, review_doc)
                    if "dealership" in review_doc:
                        # Create a Carreview object with values in `doc` object
                        print("review", review_doc["review"])
                        review_obj = DealerReview(id=review_doc["id"], name=review_doc["name"], dealership=review_doc["dealership"],
                                            review=review_doc["review"], purchase = review_doc["purchase"],
                                            purchase_date=review_doc["purchase_date"], car_make=review_doc["car_make"],
                                            car_model=review_doc["car_model"], car_year=review_doc["car_year"],
                                            another="another", sentiment=analyze_review_sentiments(review_doc["review"]))
                        results.append(review_obj)
        # For each dealer object
        
    return results

def post_request(url, json_payload, **kwargs):
    print(kwargs)
    #print("json_payload", json_payload)
    print("POST to {} ".format(url))
    try:
        response = requests.post(url, json=json_payload, params=kwargs)
        #print("Response: ", response)
        print("Posted with status {} ".format(response.status_code))
        return response
    except Exception as e:
        print(e)
        # If any error occurs
        print("Network exception occurred")
        #return response
    #return response



def post(review_dict):
    client = Cloudant.iam(
        account_name='bb42a871-2b40-4861-a11b-ece7dfaa2414-bluemix',
        api_key='Tq5P17CW558thKdS_1lV3Y1JGIcB7q8yVylP9EBlpNfH',
        connect=True)
    my_database= client["reviews"]
    try:
        my_document=my_database.create_document(review_dict["review"])
        print(my_database)
        if  my_document.exists():
            result= {
                "message":"DataInserted Successfully"
                }
        return result
    except Exception as e:
        print(e)
        return {
                'statusCode': 404,
                'message':"SomethingWent Wrong"
        }   

def analyze_review_sentiments_wrong(dealerreview, **kwargs):
    params = dict()
    params["text"] = dealerreview
    #params["version"] = kwargs["version"]
    #params["features"] = kwargs["features"]
    #params["return_analyzed_text"] = kwargs["return_analyzed_text"]
    response = requests.get(watson_service_url, params=params, headers={'Content-Type': 'application/json'},
                                    auth=HTTPBasicAuth('apikey', watson_api_key))
    return response
