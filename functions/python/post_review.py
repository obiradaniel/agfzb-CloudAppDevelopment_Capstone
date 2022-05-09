# -*- coding: utf-8 -*-
"""
Created on Sun May  8 15:25:46 2022

@author: ObiraDaniel
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May  7 21:54:42 2022

@author: ObiraDaniel
"""

import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

auth_dict = {}
auth_dict["COUCH_USERNAME"] = "bb42a871-2b40-4861-a11b-ece7dfaa2414-bluemix"
auth_dict["URL"] ="https://bb42a871-2b40-4861-a11b-ece7dfaa2414-bluemix.cloudantnosqldb.appdomain.cloud"
auth_dict["IAM_API_KEY"]= "Tq5P17CW558thKdS_1lV3Y1JGIcB7q8yVylP9EBlpNfH"

def main(dict):
    authenticator = IAMAuthenticator(auth_dict["IAM_API_KEY"])
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url(auth_dict["URL"])
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

