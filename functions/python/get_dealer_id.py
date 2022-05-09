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
    #dbs =service.get_all_dbs().result
    #['dealerships', 'guestbook', 'movies-reviews', 'reviews']
    #service.get_database_information('dealerships').result
    #service.post_all_docs(db='dealerships', include_docs=True).result
    #service.post_all_docs(db='dealerships', include_docs=True).get_result()
    #service.get_database_information('reviews').result
    if ("dealerId" not in dict) or (dict["dealerId"] == ""):
        response = service.post_all_docs(db='reviews', include_docs=True).result
    else:
        response = service.post_find(
        db='reviews',
        selector={'dealership': {'$eq': int(dict["dealerId"])}},
        ).get_result()
        """
        response = service.post_find(
        db='reviews',
        selector={
                #'dealership': {'$eq': int(dict["dealerId"])},
                "selector": {'dealership': int(dict["dealerId"])},
                "fields": [
                    "id",
                    "name",
                    "dealership",
                    "review",
                    "purchase",
                    "purchase_date",
                    "car_make",
                    "car_model",
                    "car_year"
                       ]#,
            },
        #execution_stats=True,
        use_index=["allindex"]
        ).get_result()
        """
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

#print(1, main({}))
#print(2, main({"dealerId":""}))
print(3, main({"dealerId":1}))

f=['DEFAULT_SERVICE_NAME',
 'DEFAULT_SERVICE_URL',
 'ERROR_MSG_DISABLE_SSL',
 'SDK_NAME',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_build_user_agent',
 '_convert_list',
 '_convert_model',
 '_encode_path_vars',
 '_get_system_info',
 '_set_user_agent_header',
 'authenticator',
 'configure_service',
 'default_headers',
 'delete_attachment',
 'delete_database',
 'delete_design_document',
 'delete_document',
 'delete_index',
 'delete_local_document',
 'delete_replication_document',
 'disable_retries',
 'disable_ssl_verification',
 'enable_gzip_compression',
 'enable_retries',
 'encode_path_vars',
 'get_active_tasks',
 'get_activity_tracker_events',
 'get_all_dbs',
 'get_attachment',
 'get_authenticator',
 'get_capacity_throughput_information',
 'get_cors_information',
 'get_current_throughput_information',
 'get_database_information',
 'get_db_updates',
 'get_design_document',
 'get_design_document_information',
 'get_document',
 'get_document_as_mixed',
 'get_document_as_related',
 'get_document_as_stream',
 'get_document_shards_info',
 'get_enable_gzip_compression',
 'get_geo',
 'get_geo_as_stream',
 'get_geo_index_information',
 'get_http_client',
 'get_indexes_information',
 'get_local_document',
 'get_membership_information',
 'get_partition_information',
 'get_replication_document',
 'get_scheduler_docs',
 'get_scheduler_document',
 'get_scheduler_job',
 'get_scheduler_jobs',
 'get_search_info',
 'get_security',
 'get_server_information',
 'get_session_information',
 'get_shards_information',
 'get_up_information',
 'get_uuids',
 'head_attachment',
 'head_database',
 'head_design_document',
 'head_document',
 'head_local_document',
 'head_replication_document',
 'head_scheduler_document',
 'head_scheduler_job',
 'head_up_information',
 'http_adapter',
 'http_client',
 'http_config',
 'jar',
 'new_instance',
 'post_activity_tracker_events',
 'post_all_docs',
 'post_all_docs_as_stream',
 'post_all_docs_queries',
 'post_all_docs_queries_as_stream',
 'post_api_keys',
 'post_bulk_docs',
 'post_bulk_get',
 'post_bulk_get_as_mixed',
 'post_bulk_get_as_related',
 'post_bulk_get_as_stream',
 'post_changes',
 'post_changes_as_stream',
 'post_dbs_info',
 'post_design_docs',
 'post_design_docs_queries',
 'post_document',
 'post_explain',
 'post_find',
 'post_find_as_stream',
 'post_geo_cleanup',
 'post_index',
 'post_partition_all_docs',
 'post_partition_all_docs_as_stream',
 'post_partition_find',
 'post_partition_find_as_stream',
 'post_partition_search',
 'post_partition_search_as_stream',
 'post_partition_view',
 'post_partition_view_as_stream',
 'post_revs_diff',
 'post_search',
 'post_search_analyze',
 'post_search_as_stream',
 'post_view',
 'post_view_as_stream',
 'post_view_queries',
 'post_view_queries_as_stream',
 'prepare_request',
 'put_attachment',
 'put_capacity_throughput_configuration',
 'put_cloudant_security_configuration',
 'put_cors_configuration',
 'put_database',
 'put_design_document',
 'put_document',
 'put_local_document',
 'put_replication_document',
 'put_security',
 'retry_config',
 'send',
 'service_url',
 'set_default_headers',
 'set_disable_ssl_verification',
 'set_enable_gzip_compression',
 'set_http_client',
 'set_http_config',
 'set_service_url',
 'user_agent_header']