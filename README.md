# AWS_STREAM_FIREHOSE_GLUE
The overall data ingestion from a stream application to etl process to finally target location by combining services provided by aws.

# REQUIREMENTS
1. Create a Python script that streams the records into memory, then dumps
them to an S3 bucket of yours using Kinesis Firehose (JSON).
2. Configure Kinesis Firehose to send at most 1MB of records per file
3. Write an ETL process using AWS Glue (PySpark) that has your bucket as
input and another bucket of yours as output.
4. The ETL must concatenate multiple smaller files into larger files for the
destination bucket (up to 32MB per file).
5. The ETL must change the data format to Parquet.
6. Create an EMR cluster, load the data into it, then write a Hadoop job
(MapReduce, Spark, etc, pick whichever you are comfortable with) to
compute the count of orgs across signal groups.
7. Save the results to a DynamoDB table.



# Solution
1. There are 3 folders in this repository to achieve our requirement step by step .
2. Each Folder is like a indivual component and has Readme file to understand the objective.
3. Since there are some jobs which are created by AWS CONSOLE , so to get better understanding of the story i have attached the Screenshots.
4. The order of execution to achieve our requirement are as below :-

        a) Stream_AWS_Firehose(Stream data and use AWS Kinesis firehose to dump the data as JSON onto s3 Location)
        b) AWS_Glue_ETL ( AWS Glue ETL Job which will convert JSON Small files into Bigger 35mb Parquet files and 
                dump it on another s3 location)
        c) EMR_Job ( The Pyspark Job which will run at the end on EMR , perform a use case on parquet files from 
                step-b and save the data in DynamoDB table.
        
