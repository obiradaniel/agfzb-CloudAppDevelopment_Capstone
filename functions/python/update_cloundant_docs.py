# -*- coding: utf-8 -*-
"""
Created on Wed May 18 20:03:54 2022

@author: ObiraDaniel
"""
import requests
import json
from ibmcloudant.cloudant_v1 import Document, CloudantV1
from cloudant.client import Cloudant
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from requests.auth import HTTPBasicAuth

class CarDealer:
    def __init__(self, id, city, state, st, address, zip, lat, long, short_name, full_name, totalreviews=0):
        self.id = id
        self.city = city
        self.state = state
        self.st = st
        self.address = address
        self.zip = zip
        self.lat = lat
        self.long = long
        self.short_name = short_name
        self.full_name = full_name
        self.totalreviews = totalreviews

    def __str__(self):
        return str(self.full_name) + ", Id: " + str(self.id) + ", " + str(self.city) + ", " + str(self.st)

false = False
# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, id, name, dealership, review, purchase, purchase_date, car_make, car_model, car_year, another="another", sentiment=None):
        self.id=id
        self.name=name
        self.dealership=dealership
        self.review=review
        self.purchase=purchase
        self.purchase_date=purchase_date
        self.car_make=car_make
        self.car_model=car_model
        self.car_year=car_year
        self.another=another
        self.sentiment=sentiment

    def __str__(self):
        return self.review + " " + self.car_model + " by " + self.name + ": " + self.sentiment.title()

get_dealers_url = "https://f3f2bfb2.us-south.apigw.appdomain.cloud/capstone/dealership"

get_reviews_url = "https://f3f2bfb2.us-south.apigw.appdomain.cloud/capstone/review"

post_reviews_url = "https://f3f2bfb2.us-south.apigw.appdomain.cloud/capstone/postreview"



auth_dict = {}
auth_dict["COUCH_USERNAME"] = "bb42a871-2b40-4861-a11b-ece7dfaa2414-bluemix"
auth_dict["URL"] ="https://bb42a871-2b40-4861-a11b-ece7dfaa2414-bluemix.cloudantnosqldb.appdomain.cloud"
auth_dict["IAM_API_KEY"]= "Tq5P17CW558thKdS_1lV3Y1JGIcB7q8yVylP9EBlpNfH"

authenticator = IAMAuthenticator(auth_dict["IAM_API_KEY"])
service = CloudantV1(authenticator=authenticator)
service.set_service_url(auth_dict["URL"])

client = Cloudant.iam(
        account_name='bb42a871-2b40-4861-a11b-ece7dfaa2414-bluemix',
        api_key='Tq5P17CW558thKdS_1lV3Y1JGIcB7q8yVylP9EBlpNfH',
        connect=True)

dealer_db = client["dealerships"]

#my_document=my_database.create_document(review_dict["review"])
print(dealer_db)
#my_document.exists()

def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    api_key=None
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
        
def get_all_dealer_reviews_from_cf(url):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)['body']['data']
    #print("json_result\n", json_result, "\n")
    if json_result:
        # Get the row list in JSON as dealers
        if "docs" in json_result:
            print(1)
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
                                            another="another", sentiment=None)
                        results.append(review_obj)
        else:
            print(2)
            reviews = json_result["rows"]
            #print("reviews", reviews)
            for review in reviews:
                # Get its content in `doc` object
                review_doc = review['doc']
                #print(2, review_doc)
                if "dealership" in review_doc:
                    # Create a Carreview object with values in `doc` object
                    print("review", review_doc["review"])
                    review_obj = DealerReview(id=review_doc["id"], name=review_doc["name"], dealership=review_doc["dealership"],
                                        review=review_doc["review"], purchase = review_doc["purchase"],
                                        purchase_date=review_doc["purchase_date"], car_make=review_doc["car_make"],
                                        car_model=review_doc["car_model"], car_year=review_doc["car_year"],
                                        another="another", sentiment=None)
                    results.append(review_obj)
        # For each dealer object
        
    return results

def parse_all_dealerview(all_reviews_list):
    review_count_by_id = {}
    
    for review in all_reviews_list:
        if review.dealership in review_count_by_id:
            review_count_by_id[review.dealership] = review_count_by_id[review.dealership] + 1
        else:
            review_count_by_id[review.dealership] = 1
    return review_count_by_id

def update_dealership_review_count(review_count_dic):
    doc_ids = dealer_db.all_docs()['rows']
    
    for doc_id in doc_ids:
        current_id = doc_id['id']
        db_doc = dealer_db[current_id]
        if ('address' in db_doc) and ('id' in db_doc):
            if db_doc['id'] in review_count_dic:
                db_doc['review_count'] = review_count_dic[db_doc['id']]
            else:
                db_doc['review_count'] = 0
        db_doc.save()
        print("Doc save sucessful, Id ", db_doc['id'], review_count_dic[db_doc['id']], "Reviews")
    
    print("All docs updated")
                
def main(dict):
    response = service.post_document(db='reviews', document=dict["review"]).get_result()
    try:
        # result_by_filter=my_database.get_query_result(selector,raw_result=True)
        result= {
        'headers': {'Content-Type':'application/json'},
        'body': {'data':response}
        }
        return result
    except:
        return {
        'statusCode': 404,
        'message': 'Something went wrong'
        }

doc1 = {
      "doc": {
        "_id": "61a8b600f1bb183e2c471e7a641fc188",
        "_rev": "1-34e7ebd07643af43db578a46ee1d6365",
        "address": "3 Nova Court",
        "city": "El Paso",
        "full_name": "Holdlamis Car Dealership",
        "id": 1,
        "lat": 31.6948,
        "long": -106.3,
        "short_name": "Holdlamis",
        "st": "TX",
        "state": "Texas",
        "zip": "88563"
      },
      "id": "61a8b600f1bb183e2c471e7a641fc188",
      "key": "61a8b600f1bb183e2c471e7a641fc188",
      "value": {
        "rev": "1-34e7ebd07643af43db578a46ee1d6365"
      }}


#response = service.post_document(db='products', document=products_doc).get_result()

#print(response)

t=get_all_dealer_reviews_from_cf(get_reviews_url)

y = parse_all_dealerview(t)

update_dealership_review_count(y)