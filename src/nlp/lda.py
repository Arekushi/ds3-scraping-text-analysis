from pyspark.sql.functions import udf, col
from pyspark.sql.types import ArrayType, StringType
from pyspark.ml.clustering import LDA


num_topics = 3
max_iter = 50
num_top_words = 25
seed = 2022


def lda_train(tfidf_result):
    lda = LDA(
        k=num_topics,
        maxIter=max_iter,
        seed=seed,
        featuresCol='tf_idf_features',
    )
    lda_model = lda.fit(tfidf_result)
    lda_result = lda_model.transform(tfidf_result)

    return lda_model, lda_result


# def show_topics(cleaned_df):
#     tf_model, tf_result, tfidf_model, tfidf_result = vectorization(cleaned_df)
#     lda_model, lda_result = lda_train(tfidf_result)
#
#     vocab = tf_model.vocabulary
#
#     def get_words(token_list):
#         return [vocab[token_id] for token_id in token_list]
#
#     topics = lda_model\
#         .describeTopics(num_top_words)\
#         .withColumn('topicWords', udf(get_words, ArrayType(StringType()))(col('termIndices')))
#
#     topics.select('topic', 'topicWords').show(truncate=False)
