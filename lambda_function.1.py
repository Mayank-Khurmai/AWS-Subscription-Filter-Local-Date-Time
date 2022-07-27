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

def lambda_handler(event, context):
    return_response_code = int(event['return_response_code'])
    
    if(return_response_code == 200):
        logger.info("Response_code=" + str(return_response_code))
        return return_response_code
    elif(return_response_code == 400):
        logger.info("Response_code=" + str(return_response_code))
        return return_response_code
    else:
        return "Something Other"