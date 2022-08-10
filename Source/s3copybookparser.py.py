import io
import json
import boto3
import logging
import sys
import copybook

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
s3 = boto3.client('s3')

#Folowing Global Variables received from the step function
    # 1. s3_source_bucket_name - S3 Bucket Name of Data File 
    # 2. s3_source_bucket_key - Name of Data File along with path
    # 3. s3_copybook_bucket_name - S3 Bucket Name of Copybook
    # 4. s3_copybook_bucket_key - Name of the s3 copybook
    # 5. Derived_Table_Name - Athena Table Name to created. This is formatted name of the s3_copybook_bucket
    # 6. Derived_Table_Definition - Athena Table definition created in s3coppybookparser.py

def lambda_handler(event, context):

    Copybook_Bucket = event['s3_copybook_bucket_name'] 
    Copybook_file = event['s3_copybook_bucket_key']
    Datafile_Bucket = event['s3_source_bucket_name']
    Data_file = event['s3_source_bucket_key']
    
    #Derived Variable Definition from Data/Copybook Names
    TableName = Copybook_file.replace("/","_").replace(".","_")
    Location = "s3://" + Datafile_Bucket + "/input"  #Data File
    
    Derived_Table_Name  = TableName


    result = s3.get_object(Bucket=Copybook_Bucket, Key=Copybook_file)["Body"].read().decode(encoding="utf-8",errors="ignore")
    output = copybook.toDict(result.splitlines())
    #print(output)

    copybook.altlay = []
    copybook.transf = []
    copybook.lrecl = 0
    copybook.transf1 = []
    copybook.transf2 = []
    copybook.CreateExtraction(output)
    
    #Create Defn Template
    Tablevariable=str(copybook.transf1).replace("'","").replace("[","").replace("]","").replace("-","_")
    Tablebytes=str(copybook.transf2).replace("'","").replace("[","").replace("]","").replace(",","")
    
    outputlayout1 = " CREATE EXTERNAL TABLE IF NOT EXISTS " + TableName + " (" + Tablevariable + " )"
    outputlayout2 = " ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe'"
    outputlayout3 = " WITH SERDEPROPERTIES ( " + '"input.regex"' +  " = " + '"' + Tablebytes.replace(" ","")  + '"' +")"
    outputlayout4 = " LOCATION " + "'" + Location + "'"

    FinalTableDefinition = outputlayout1 + outputlayout2 + outputlayout3 +  outputlayout4
    
    print(FinalTableDefinition)
    Derived_Table_Definition = FinalTableDefinition

    #pass through values
    return {
        's3_copybook_bucket_name': event['s3_copybook_bucket_name'],
        's3_copybook_bucket_key': event['s3_copybook_bucket_key'],
        's3_source_bucket_name': event['s3_source_bucket_name'],
        's3_source_bucket_key': event['s3_source_bucket_key'],
        'Derived_Table_Name': Derived_Table_Name,
        'Derived_Table_Definition': Derived_Table_Definition
  
            }