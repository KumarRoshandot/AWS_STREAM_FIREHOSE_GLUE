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
