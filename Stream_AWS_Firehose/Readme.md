# This is the starting point in overall ingestion process 

1. The Data is coming from CSV FILE which is being fed by Python memory streamwise fashion to AWS Kinesis FireHose.
2. To Use Firehose first a Delivery Stream app has to be created via AWS Console or its SDK.
3. I have created a Firehose Delivery Stream 'stream_predict_s3' via AWS Console , the snapshot is attached in sequential manner to understand the properties of a Stream.
4. In Order to create a Firehose Delivery Stream you need following things ready:-

               a) An S3 Bucket 'firehose-aws-us-ae1-raw' where the Delivery Stream will dump the raw data 
                  coming in stream fashion.
               b) A Lambda Function 'kinesis-firehose-csv-stream-to-json' ( AWS Lambda ) which will 
                  convert the CSV Data to JSON Data before dumping into S3 Location.

5. Now once the streaming starts the source (CSV-python job memory) will stream data into 'stream_predict_s3' which will trigger lambda 'kinesis-firehose-csv-stream-to-json' which will convert data into JSON at run time , which then eventually be dumped to s3 Location ('firehose-aws-us-ae1-raw).


## There are 2 scripts attached with this folder 
1. First is the Python script (stream_s3_firehose.py) which reads the CSV File from a location and stream in memory and pass it over to Firehose Delivery Stream 'stream_predict_s3'.
2. A Lambda Function Python Script which will take the payload coming from 'stream_predict_s3' , converts it to JSON and Return the data to again 'stream_predict_s3'.

  Once the JSON Data has come to 'stream_predict_s3' it will dump the data to S3 Location 'firehose-aws-us-ae1-raw' which is already configured in 'stream_predict_s3' before hand.
  
  
  Please Refer to the attached snapshot and python script for understanding.!!!
