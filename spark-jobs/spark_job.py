import sys
import re
import os
from pyspark.sql.types import StructType, StructField, StringType, FloatType, IntegerType, TimestampType
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp


def main(input_path, output_table):
    spark = SparkSession.builder \
        .appName("GCS to BigQuery Test") \
        .getOrCreate()

    schema = StructType([
                StructField("Timestamp", TimestampType(), True),
                StructField("Type_of_mobile", StringType(), True),
                StructField("MMSI", IntegerType(), True),
                StructField("Latitude", FloatType(), True),
                StructField("Longitude", FloatType(), True),
                StructField("Navigational_status", StringType(), True),
                StructField("ROT", FloatType(), True),
                StructField("SOG", FloatType(), True),
                StructField("COG", FloatType(), True),
                StructField("Heading", FloatType(), True),
                StructField("IMO", StringType(), True),
                StructField("Callsign", StringType(), True),
                StructField("Name", StringType(), True),
                StructField("Ship_type", StringType(), True),
                StructField("Cargo_type", StringType(), True),
                StructField("Width", FloatType(), True),
                StructField("Length", FloatType(), True),
                StructField("Type_of_position_fixing_device", StringType(), True),
                StructField("Draught", FloatType(), True),
                StructField("Destination", StringType(), True),
                StructField("ETA", StringType(), True),
                StructField("Data_source_type", StringType(), True),
                StructField("A", FloatType(), True),
                StructField("B", FloatType(), True),
                StructField("C", FloatType(), True),
                StructField("D", FloatType(), True)
])

    df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(input_path) \
    .repartition(3)

    print("Columns in the DataFrame: ", df.columns)

    df = df.withColumnRenamed("# Timestamp", "Timestamp")
    df = df.withColumn("Timestamp", to_timestamp(col("Timestamp"), "dd/MM/yyyy HH:mm:ss"))

    new_column_names = [c.replace(" ", "_").lower() for c in df.columns]

    for old_name, new_name in zip(df.columns, new_column_names):
        df = df.withColumnRenamed(old_name, new_name)
  

    # Specify the GCS bucket for intermediate storage
    bucket = os.getenv('INTERMEDIATE_GCS_BUCKET', 'default-intermediate-bucket')
    temporaryGcsBucket = f"gs://{bucket}"

    # Write to BigQuery
    df.write.format('bigquery') \
        .option('temporaryGcsBucket', temporaryGcsBucket) \
        .option('table', output_table) \
        .option('partitionField', 'Timestamp') \
        .option('clusteredFields', 'ship_type,cargo_type') \
        .option("dataSource", "com.google.cloud.spark.bigquery.v2.Spark34BigQueryTableProvider") \
        .mode('append') \
        .save()

    spark.stop()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: spark_job.py <input_path> <output_table>", file=sys.stderr)
        exit(-1)
    main(sys.argv[1], sys.argv[2])