# This is the Second Point in the overall ingestion Process

1.Now the Data is Present in s3 Location 'firehose-aws-us-ae1-ss3-raw' from Firehose Delivery Stream.

2.Next is to take this JSON Small files and merge it into bigger files 35 mb and load it onto another s3 bucket 'firehose-aws-us-ss3-raw-parquet' as parquet type.

3.To achieve it AWS GLue ETL job is Created (another AWS Service).

4.AWS Glue ETL job requires following things:-

    a) A Crawler , Its a component in AWS GLue which will scan the Input file and derive a Schema out of it and 
        then save the schema in some s3 location as a table (Crawler can be created on Glue UI , again from Console).
    b) A Source Location , A target Location.
    
5.Once your crawler is done , you can run the crawler and get a schema file for your source file , which will be used in Glue ETL job.

6.Again from AWS COnsole , create a ETL job in Glue UI , its all step by step wizard.

7.Once you create a ETL job a Pyspark Script will be created , in which you can modify any ETL logic , in my case i have added a property 'groupsize' which will control the 35mb size of target file.

8.Once this ETL job runs it will create a parquet files in s3 location 'firehose-aws-us-ss3-raw-parquet'.


Please refer attached files with this folder for better understanding.
