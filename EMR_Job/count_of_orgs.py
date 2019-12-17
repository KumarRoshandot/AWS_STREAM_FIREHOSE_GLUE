from pyspark.sql import SparkSession
import sys

spark = SparkSession \
    .builder \
    .appName("Count Of Orgs") \
    .enableHiveSupport() \
    .getOrCreate()

sc = spark.sparkContext
spark.sql("SET spark.sql.hive.convertMetastoreOrc=true")
spark.sql("SET spark.sql.orc.enabled=true")


def main():
    try:
        # Checking Parameter passed
        total_arg = len(sys.argv) - 1
        if total_arg >= 1:
            input_s3_loc = sys.argv[1]
        else:
            print("Invalid Arguments passed ")
            sys.exit(0)

        '''
        Main Logic to derive all fields based on joins.
        1) Load everything on spark, whatever is there on this planet
        2) Create all the columns that need to be derived like valuation_start_date , valuation_end_date , current_flag etc..
        3) create spark table for each base dataframe , Df.createOrReplaceTempView("<SPARK_TABLE_NAME>")---> Do it for all Dataframe
        4) DF_RESULT = spark.sql("MAIN SQL QUERY, WRITE ALL JOINS ")
        5) De-Standardize any column of tpa specific which is required. 
        6) Cast al the columns to its appropiate data type as per unified_staging table
        7) Club it with old unified Staging data and write the overall data to staging table as overwrite
        8) Delete HDFS Files 
        '''
        source_df = spark.read.parquet(input_s3_loc)
        source_df.createOrReplaceTempView("INPUT_TABLE")

        sql = '''
        Select
        signal,
        orgs,
        count(*) as count_of_orgs_across_signals
        from INPUT_TABLE
        group by signal,orgs
        '''

        source_df = spark.sql(sql)
        source_df.createOrReplaceTempView("FINAL_TABLE")
        spark.sql("INSERT OVERWRITE TABLE temp SELECT * FROM FINAL_TABLE")

    except Exception as e:
        print('Exception Occured in main , Line no {}:-'.format(sys.exc_info()[-1].tb_lineno), str(e))


if __name__ == "__main__":
    main()