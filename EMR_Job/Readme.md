# This is the last point for data ingestion process.

1.This is a Pyspark Job which will run on EMR which will take files from s3 'firehose-aws-us-ss3-raw-parquet' and derive the count of organisations across signals and save it on DynamoDB table.

2.Since Its a Pyspark job , there was an issue making direct connectivity to DynamoDB , so to save data on dynamoDB i have taken the hive route.

3. Following is the Steps that is required :- 

        a) Create a temporary hive table like

            CREATE TABLE TEMP(
                  column1 type,
                  column2 type...)
            STORED AS ORC;

        b) Run your pySpark job and write your data to it

          dataframe.createOrReplaceTempView("df")
          spark.sql("INSERT OVERWRITE TABLE temp SELECT * FROM df")

        c) Create the dynamo connector table

            CREATE TABLE TEMPTODYNAMO(
                column1 type,
                column2 type...)
            STORED BY 'org.apache.hadoop.hive.dynamodb.DynamoDBStorageHandler'
            TBLPROPERTIES ("dynamodb.table.name" = "temp-to-dynamo",
            "dynamodb.column.mapping" = "column1:column1,column2:column2...";

        d) Overwrite that table with your temp table

            INSERT OVERWRITE TABLE TEMPTODYNAMO SELECT * FROM TEMP;
            
   
   4. For spark to DynamoDB connectivity , there are connectors available but mostly for SCALA code.
