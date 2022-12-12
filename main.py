from time import time
from src.nlp import clean_dataframe, py_ldavis, word_cloud_from_lda, \
    vectorization, lda_train, get_session


def main():
    start = time()

    spark = get_session()
    df = clean_dataframe(spark)
    tf_model, tf_result, tfidf_model, tfidf_result = vectorization(df)
    lda_model, lda_result = lda_train(tfidf_result)

    word_cloud_from_lda(tf_model, lda_model)
    py_ldavis(df, tf_model, lda_result, lda_model)

    end = time()
    print('It took', (end - start), 'seconds')


if __name__ == '__main__':
    main()
