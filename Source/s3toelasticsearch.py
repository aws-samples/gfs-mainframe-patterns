import os
import csv
import json
import boto3
import traceback 
import sys
import codecs
import logging
import uuid
from elasticsearch import Elasticsearch, RequestsHttpConnection, helpers
from requests_aws4auth import AWS4Auth 
from opensearchpy import OpenSearch


config_file = "config.json"
metadata_file = "metadata.json"
bulk_batch_size = 100

"""
Can Override the global variables using Lambda Environment Parameters
"""
# globalVars = {}
# globalVars['Environment'] = "Prod"
# globalVars['awsRegion'] = "us-east-2"
# globalVars['tagName'] = "serverless-s3-to-es-log-ingester"
# globalVars['service'] = "es"
# globalVars['esIndexPrefix'] = "s3-to-es-"
# globalVars['esIndexDocType'] = "s3_to_es_docs"

# host = "https://search-essearch-3h4uqclifeqaj2vg4mphe7ffle.us-east-2.es.amazonaws.com"

# Initialize Logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)



def lambda_handler(event, context):
    
    # response = s3toes.main()
        
    # Initialize S3 Object received from event trigger
    #-------------------------------------------------
    # logger.info("Received event: " + json.dumps(event, indent=2))
    s3 = boto3.client('s3')
    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key =    event['Records'][0]['s3']['object']['key']
        # bucket = 'athenas3toelasticsearch'
        # key = 'mockedcopydata.csv'

        # Get documet (obj) form S3
        obj = s3.get_object(Bucket=bucket, Key=key)
    
    except Exception as e:
        logger.error('ERROR: {0}'.format(str(e)))
        logger.error(
            'ERROR: Unable able to GET object:{0} from S3 Bucket:{1}. Verify object exists.'.format(key, bucket))
    
    # Get Credentials
    # credentials = boto3.Session().get_credentials()
    # awsauth = AWS4Auth(credentials.access_key,
    #                   credentials.secret_key,
    #                   globalVars['awsRegion'],
    #                   globalVars['service'],
    #                   session_token=credentials.token
    #                   )

    # print("HOST=",os.environ.get('HOST')) 
    # print("HOST=",os.environ.get('AWS_REGION')) 
    
    
    #Establish connection with Open Search Service
    #---------------------------------------------
    try:
        host = os.environ.get('HOST')
        access_key = os.environ.get('ACCESS_KEY')
        secret_key = os.environ.get('SECRET_KEY')
        awsauth = AWS4Auth(access_key, secret_key, 'us-east-2', 'es')
        
        es = Elasticsearch(
                hosts=[{'host': host, 'port': 443}],
                http_auth=awsauth,
                use_ssl=True,
                verify_certs=True,
                connection_class=RequestsHttpConnection
                )
        es.ping()
        
            
    except Exception as e:
        print("Unknown error exception")
        traceback.print_exc()
        sys.exit(2)
        
    # Initialize S3 CSV Object
    #----------------------
    csv_obj = obj
    body = csv_obj['Body']
    csv_string = csv.DictReader(codecs.getreader("utf-8-sig")(body))
    print("csv_string",csv_string)
    
    #Read CSV Data Rows, Batch it up and push to elastic search index in bulk mode
    #-----------------------------------------------------------------------------
    #Set Index Meta Data # File name as Index Name
    filename=key.lower()
    Index = filename.replace("results/input_","")
    
    ## batch control
    row_count = 0
    
    ## bulk actions
    actions = []
    
    for row in csv_string:
        row_id = row_count
        # es.index(Index, id=row_count,body=json.dumps(row)) 
        source_dict = json.dumps(row)
        
        # define a document
        es_doc = {
            "_index": Index,
            "_id": row_id,
            "_source": source_dict
            #"_source": data_row  
        }
        actions.append(es_doc)
    
        # increase batch size
        row_count += 1

            # batch process
        if row_count % bulk_batch_size == 0:
            bulk_es(es, actions)
            actions = []
            
    # final batch size
    bulk_es(es, actions)
    print("INFO: Bulk write succeed: {} documents".format(row_count))
    
def bulk_es(es, data: dict):
    # bulk process
    try:
        print("Number of processing documents: {}".format(len(data)))
        res = helpers.bulk(es, data)
        print("Bulk write succeed: {} documents".format(res[0]))
    except helpers.errors.BulkIndexError as be:
        print("Bulk error: {}".format(str(be)))
    except Exception as e:
        print("Exception: {}".format(str(e)))
        traceback.print_exc()
        sys.exit(2)
        

    

# if __name__ == '__main__':
#     lambda_handler(None, None)