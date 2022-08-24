import time
import boto3
import logging
import datetime
now = datetime.datetime.now()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')

#Folowing Global Variables received from the step function
    # 1. s3_source_bucket_name - S3 Bucket Name of Data File 
    # 2. s3_source_bucket_key - Name of Data File along with path
    # 3. s3_copybook_bucket_name - S3 Bucket Name of Copybook
    # 4. s3_copybook_bucket_key - Name of the s3 copybook
    # 5. Derived_Table_Name - Athena Table Name to created. This is formatted name of the s3_copybook_bucket
    # 6. Derived_Table_Definition - Athena Table definition created in s3coppybookparser.py



#COLUMN = 'your_column_name'


def lambda_handler(event, context):

    # athena constant
    DATABASE = 'fileaiddemo' # This is fixed for easy maitenance 
    TABLE = ""+ event['Derived_Table_Name'] +"" # Passed from Previous Copybook Parser Program
    #TABLE = 'copybook_employee_cpy'
    #Create_Table_Defn = """CREATE EXTERNAL TABLE IF NOT EXISTS copybook_employee_cpy (EMP_NUMBER int, EMP_LAST_NAME string, EMP_FIRST_NAME string, EMP_MID_INIT string, FILLER_1 string, EMP_TITLE string, EMP_NAIL_ID string, FILLER_2 string, EMP_DOB string ) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe' WITH SERDEPROPERTIES ( "input.regex" = "(.{5}) (.{15}) (.{25}) (.{1}) (.{2}) (.{30}) (.{9}) (.{1}) (.{10})")  LOCATION 's3://fileaid-demoinput/employee.txt'"""
    Create_Table_Defn = "" + event['Derived_Table_Definition'] + ""
    
    #Pass to the above variable
    
    # S3 constant - This temperory folders for Athena Usage. So we are utilizing the copybook bucket for this purpose
    S3_OUTPUT = 's3://' + event['s3_copybook_bucket_name'] + '/output/' #s3_copybook_bucket + "/output"
    S3_BUCKET = 's3://' + event['s3_copybook_bucket_name'] + '/query/' #s3_copybook_bucket + "/query"
    DataFile = event['s3_source_bucket_key'] #this s3 data file name passed from step function.  s3_source_bucket_key 
    DataFile_Formatted = DataFile.replace("-","_").replace("/","_").replace(".","_").replace("_txt","")
    
        #Creatimng WHERE Clause
    COLUMN = '"$path"'
    keyword = 's3://' + event['s3_source_bucket_name'] + '/' + event['s3_source_bucket_key']
    
    # number of retries
    RETRY_COUNT = 10
    
    # athena client
    client = boto3.client('athena')
    
  
    #--------------Create Database -  Query Execution-------------------    
    response = client.start_query_execution(
    QueryString='create database if not exists fileaiddemo',
    ResultConfiguration={'OutputLocation': S3_BUCKET})
    print("create table=",response)
    
    
    #--------------Create Table Query Execution-------------------
    response = client.start_query_execution(
        QueryString= Create_Table_Defn,
        QueryExecutionContext={
            'Database': DATABASE
        },
        ResultConfiguration={
            'OutputLocation': S3_BUCKET
        }
    )
    print("create table=",response)
    
    
    # -----------get query execution id and get status----------
    query_execution_id = response['QueryExecutionId']
    time.sleep(1)
    query_status = client.get_query_execution(QueryExecutionId=query_execution_id)
    query_execution_status = query_status['QueryExecution']['Status']['State']
    if query_execution_status == 'SUCCEEDED':
            print("Create Table - STATUS:" + query_execution_status)
      
    if query_execution_status == 'FAILED':
            raise Exception("Create Table - STATUS:" + query_execution_status)

    else:
            print("Create Table - STATUS:" + query_execution_status)
    
    
    #-------------- Select query Execution------------------------------------
    query = "SELECT * FROM %s.%s where %s = '%s';" % (DATABASE, TABLE, COLUMN, keyword)
    #query = "UNLOAD (SELECT * FROM copybook_organization_cpy)  WITH (format = 'JSON');"
  

    # Execution of Select Query
    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': DATABASE
        },
        ResultConfiguration={
            'OutputLocation': S3_OUTPUT
        }
    )

    # get query execution id
    query_execution_id = response['QueryExecutionId']
    filename = query_execution_id 
    print("query_execution_id=",query_execution_id)
    
    
    
    
    # Executes query and waits 3 seconds
    queryId1 = response['QueryExecutionId']
    time.sleep(3)
    print("queryId1=",queryId1)
    
    # get execution status
    for i in range(1, 1 + RETRY_COUNT):

        # get query execution
        query_status = client.get_query_execution(QueryExecutionId=query_execution_id)
        query_execution_status = query_status['QueryExecution']['Status']['State']

        if query_execution_status == 'SUCCEEDED':
            print("Select Query - STATUS:" + query_execution_status)
            break

        if query_execution_status == 'FAILED':
            raise Exception("Select Query - STATUS:" + query_execution_status)

        else:
            print("Select Query - STATUS:" + query_execution_status)
            time.sleep(i)
    else:
        client.stop_query_execution(QueryExecutionId=query_execution_id)
        raise Exception('TIME OVER')

    # get query results
    result = client.get_query_results(QueryExecutionId=query_execution_id)
  

    #copies newly generated csv file with appropriate name
    #query result output location you mentioned in AWS Athena
    print(filename)
    queryLoc = event['s3_copybook_bucket_name']  + "/output/" + queryId1 + ".csv"
    print(queryLoc)
    #destination location and file name
    # s3_resource.Object('athenaresultstoes','Results/'+ DataFile_Formatted + '.csv').copy_from(CopySource = queryLoc) This is changed to make the results in the same bucket
    s3_resource.Object(event['s3_copybook_bucket_name'],'results/'+ DataFile_Formatted + '.csv').copy_from(CopySource = queryLoc)
    
    #deletes Athena generated csv and it's metadata file 
    response = s3_client.delete_object(
        Bucket=event['s3_copybook_bucket_name'] ,
        Key="/output/" + filename + ".csv"
    )
   
    response = s3_client.delete_object(
        Bucket=event['s3_copybook_bucket_name'] ,
        Key="/output/" + filename + ".csv.metadata"
    )
    


    # get data
    # if len(result['ResultSet']['Rows']) == 2:

    #     email = result['ResultSet']['Rows'][1]['Data'][1]['VarCharValue']

    #     return email

    # else:
    #     return None
    
    result_file_key = "results/"+ DataFile_Formatted + ".csv"
        #pass through values
    return {
        's3_result_bucket_name': event['s3_source_bucket_name'],
        's3_result_file_key': result_file_key
  
            }