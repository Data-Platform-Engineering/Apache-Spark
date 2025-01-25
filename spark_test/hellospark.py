from pyspark.sql import SparkSession
from pyspark.sql.functions import to_timestamp, col
from data_generator import data_generator

spark = SparkSession.builder.appName("HelloSpark").getOrCreate()

data = data_generator(1000)

df = spark.createDataFrame(data)

df_filtered = df.select(
    "address",
    "agency_responsible",
    "closed_date",
    "data_as_of",
    "data_loaded_at",
    "lat",
    "long",
    "point",
    "point_geom",
    "requested_datetime",
    "service_details",
    "service_name",
    "service_request_id",
    "service_subtype",
    "source",
    "status_description",
    "status_notes",
    "updated_datetime",
    "analysis_neighborhood",
    "bos_2012",
    "media_url",
    "neighborhoods_sffind_boundaries",
    "police_district",
    "street",
    "supervisor_district"
)

df_filtered = (
    df_filtered.withColumn("closed_date", to_timestamp(col("closed_date"), "MM/dd/yyyy hh:mm:ss a"))
    .withColumn("data_as_of", to_timestamp(col("data_as_of"), "MM/dd/yyyy hh:mm:ss a"))
    .withColumn("data_loaded_at", to_timestamp(col("data_loaded_at"), "MM/dd/yyyy hh:mm:ss a"))
    .withColumn("requested_datetime", to_timestamp(col("requested_datetime"), "MM/dd/yyyy hh:mm:ss a"))
    .withColumn("updated_datetime", to_timestamp(col("updated_datetime"), "MM/dd/yyyy hh:mm:ss a"))
    .withColumn("lat", col("lat").cast("double"))
    .withColumn("long", col("long").cast("double"))
)


# TODO : output the transformed data to an s3 bucket

df_filtered.printSchema()

