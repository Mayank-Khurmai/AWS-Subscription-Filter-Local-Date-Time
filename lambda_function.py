import json
import boto3
import gzip
import base64
import datetime
import time
import logging
from dateutil import tz

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def base64_decomprress(cw_event):
    cw_event = cw_event['awslogs']['data']
    cw_event_b64_decode = base64.b64decode(cw_event)
    decompressed_data  = gzip.decompress(cw_event_b64_decode)
    final_event = json.loads(decompressed_data)
    return final_event
    
def filter_cw_event(cw_event):
    cw_eventm = cw_event.replace("\n", "")
    return cw_event

def date_time_ist():
    from_zone = tz.tzutc()
    to_zone = tz.gettz('Asia/Kolkata')
    utc_time = datetime.datetime.now()
    utc_time = utc_time.replace(tzinfo=from_zone)
    date_time = utc_time.astimezone(to_zone)
    date_time = str(date_time)
    return date_time
        
def lambda_handler(event, context):
    cw_event  = base64_decomprress(event)
    # cw_event = filter_cw_event(cw_event)
    # cw_event = json.dumps(event)
    date_time = date_time_ist()
    logger.info("Log Created At - "+ str(date_time))
    
    # s3 = boto3.client('s3');
    # bucket_name = 'cloudwatch-logs-test-mayank'
    # location = 'cloudwatch-sf-lambda-s3/'+date_time+'.json'
    # s3.put_object(Body=cw_event, Bucket=bucket_name, Key=location)
    
    x =  {
        "aws-log-400": str(cw_event)
    }
    logger.info("Loggggggg----"+ str(x))
    return x
    