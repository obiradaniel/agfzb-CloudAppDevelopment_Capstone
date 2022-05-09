#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests

auth_dict = {}
auth_dict["COUCH_USERNAME"] = "bb42a871-2b40-4861-a11b-ece7dfaa2414-bluemix"
auth_dict["IAM_API_KEY"]= "Tq5P17CW558thKdS_1lV3Y1JGIcB7q8yVylP9EBlpNfH"

def main(dict):
    databaseName = "dealerships"

    try:
        client = Cloudant.iam(
            account_name=dict["COUCH_USERNAME"],
            api_key=dict["IAM_API_KEY"],
            connect=True,
        )
        print(1)
        print("Databases: {0}".format(client.all_dbs()))
    except CloudantException as ce:
        print(2)
        print("unable to connect")
        return {"error": ce}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print(3)
        print("connection error")
        return {"error": err}

    return {"dbs": client.all_dbs()}

out = main(auth_dict)