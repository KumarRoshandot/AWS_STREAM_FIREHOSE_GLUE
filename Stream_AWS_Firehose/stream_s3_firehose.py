# Import the SDK
import boto3
import logging
from botocore.exceptions import ClientError
import sys
import csv

def get_data(input_filename,delimiter = ';'):
    with open(input_filename, 'r+b') as f:
        reader = csv.DictReader(f,quotechar='"',delimiter=delimiter)
        for record in reader:
            #x = record.split(delimiter)
            yield record


def send_data(firehose_name,input_filename):
    client = boto3.client('firehose')
    try:
        response = client.put_record(
            DeliveryStreamName=firehose_name,
            Record={
                'Data': get_data(input_filename)
            }
        )
        logging.info(response['MessageId'])
    # Display an error if something goes wrong.
    except ServiceUnavailableException as e:
        pass
    except ClientError as e:
        logging.error(e.response['Error']['Message'])
        logging.error(e)
    else:
        logging.info("Email sent! ErrorCode ID:"),
        logging.info(response['ErrorCode'],response['ErrorMessage'])


if __name__ == "__main__":
    # Input file with absolute path
    input_filename = sys.argv[1]

    # This is the Kinesis Fire Hose delivery stream name, created via aws console
    firehose_name = 'stream_predict_s3'

    # This will dump data to s3 as JSON from stream of csv data
    send_data(firehose_name,input_filename)
