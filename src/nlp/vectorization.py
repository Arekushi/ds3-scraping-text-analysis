from pyspark.ml.feature import CountVectorizer, IDF


def vectorization(clean_df):
    tf_model, tf_result = count_vectorizer(clean_df)
    tfidf_model, tfidf_result = idf(tf_result)
    return tf_model, tf_result, tfidf_model, tfidf_result


# a frequência de cada termo em um documento
def count_vectorizer(df_clean):
    tfizer = CountVectorizer()\
            .setInputCol('final')\
            .setOutputCol('tf_features')

    tf_model = tfizer.fit(df_clean)
    tf_result = tf_model.transform(df_clean)
    return tf_model, tf_result


# frequência inversa dos documentos onde ocorreu um termo
def idf(tf_result):
    tfidf = IDF()\
        .setInputCol('tf_features')\
        .setOutputCol('tf_idf_features')

    tfidf_model = tfidf.fit(tf_result)
    tfidf_result = tfidf_model.transform(tf_result)
    return tfidf_model, tfidf_result
