import nltk
from pyspark.sql import functions as f
from pyspark.ml import Pipeline
from sparknlp import Finisher
from sparknlp.annotator import LemmatizerModel, Stemmer, Tokenizer, StopWordsCleaner,\
    Normalizer, PerceptronModel, Chunker
from sparknlp.base import DocumentAssembler
from nltk.corpus import stopwords

from config import settings
from src.scraping import load_weapons, transform_weapons


finisher_columns = (
    'unigrams',
    # 'ngrams'
)


def clean_dataframe(spark):
    df = get_df(spark)

    nlp_pipeline = Pipeline().setStages([
        doc_assembler(),
        tokenizer(),
        normalizer(),
        lemmatizer(),
        stopwords_cleaner(),
        pos_tagger(),
        chunker(),
        finisher()
    ])

    clean_df_result = nlp_pipeline.fit(df).transform(df)

    final_df = clean_df_result.withColumn(
        'final', f.concat(
            *[f.col(f'finished_{column}') for column in finisher_columns]
        )
    )

    return final_df


def get_df(spark):
    weapons = transform_weapons(load_weapons())
    columns = settings.dataframe_columns
    n = len(columns)
    df_weapons = spark.createDataFrame(weapons[0:n], columns)

    df_weapons = df_weapons.withColumn(
        'text',
        f.concat(
            *[f.col(column) for column in columns[1:n]]
        )
    )

    return df_weapons


def doc_assembler():
    return DocumentAssembler()\
        .setInputCol('text')\
        .setOutputCol('document')\
        .setCleanupMode('shrink')


def tokenizer():
    return Tokenizer()\
        .setInputCols(['document'])\
        .setOutputCol('tokenized')


def normalizer():
    return Normalizer()\
     .setInputCols(['tokenized'])\
     .setOutputCol('normalized')\
     .setLowercase(True)


def lemmatizer():
    return LemmatizerModel.pretrained()\
        .setInputCols(['normalized'])\
        .setOutputCol('lemmatized')


def stopwords_cleaner():
    nltk.download('stopwords')
    eng_stopwords = stopwords.words('english')
    eng_stopwords.extend(settings.stop_words)

    return StopWordsCleaner()\
        .setInputCols('lemmatized')\
        .setOutputCol('unigrams')\
        .setStopWords(eng_stopwords)


def pos_tagger():
    return PerceptronModel.pretrained('pos_anc') \
        .setInputCols(['document', 'lemmatized']) \
        .setOutputCol('pos')


def chunker():
    allowed_tags = [
        '<JJ>+<NN>',
        '<NN>+<NN>'
    ]

    return Chunker()\
        .setInputCols(['document', 'pos'])\
        .setOutputCol('ngrams')\
        .setRegexParsers(allowed_tags)


def finisher():
    return Finisher()\
        .setInputCols(*finisher_columns)
