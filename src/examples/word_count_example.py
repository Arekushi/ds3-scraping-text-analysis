# type: ignore
from operator import add
from pyspark.sql import SparkSession
import findspark


def main():
    findspark.init()

    spark = SparkSession.builder \
        .master('local') \
        .appName('Word Count') \
        .getOrCreate()
    sc = spark.sparkContext

    inputfile = sc.textFile("./data/word-count/lorem_ipsum.txt")
    counts = inputfile.flatMap(lambda l: l.split(' '))\
        .map(lambda w: (w, 1))\
        .reduceByKey(add)\
        .sortBy(lambda x: x[1], ascending=False)
    output = counts.collect()

    for word, count in output:
        print(f'Word: {word} | Count: {count}')

    sc.stop()
    spark.stop()


if __name__ == "__main__":
    main()
