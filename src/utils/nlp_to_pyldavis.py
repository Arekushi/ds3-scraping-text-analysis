import numpy as np
from pyspark.sql import DataFrame
from pyspark.sql.functions import explode, size


def format_data_to_pyldavis(cleaned_df: DataFrame, tf_model, lda_result, lda_model):
    df = cleaned_df.select('final').final
    counts = cleaned_df.select((explode(df)).alias('tokens')).groupby('tokens').count()

    wc = {i['tokens']: i['count'] for i in counts.collect()}
    wc = [wc[x] for x in tf_model.vocabulary]

    data = {
        'topic_term_dists': np.array(lda_model.topicsMatrix().toArray()).T,
        'doc_topic_dists': np.array(
            [x.toArray() for x in lda_result.select(['topicDistribution']).toPandas()['topicDistribution']]
        ),
        'doc_lengths': [x[0] for x in cleaned_df.select(size(df)).collect()],
        'vocab': tf_model.vocabulary,
        'term_frequency': wc
    }

    return data
