from pyspark.sql import SparkSession
from config import settings


def get_session():
    spark = SparkSession.builder\
        .appName('ds3-weapons-text-analysis')\
        .config('spark.driver.memory', '8G')\
        .config('spark.driver.maxResultSize', '2G')\
        .config('spark.kryoserializer.buffer.max', '500m')\
        .config('spark.worker.cleanup.enabled', 'true')\
        .config('spark.jars', settings.spark_nlp_jar_path)\
        .config('spark.local.dir', settings.spark_local_dir)\
        .getOrCreate()

    return spark
