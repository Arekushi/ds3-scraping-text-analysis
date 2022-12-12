from time import time

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from wordcloud import WordCloud

from config import settings
from src.utils.path_utils import make_dir


path = settings.word_clouds_pdf_path


def word_cloud_from_lda(tf_model, lda_model):
    vocab = tf_model.vocabulary
    topics = lda_model.describeTopics(maxTermsPerTopic=100)

    topics_words = topics.rdd \
        .map(lambda row: row['termIndices']) \
        .map(lambda idx_list: [vocab[idx] for idx in idx_list]) \
        .collect()

    save_pdf(topics_words)


def save_pdf(topics_words):
    file_name = f'out-{int(time())}.pdf'
    make_dir(path)

    with PdfPages(f'{path}/{file_name}') as pdf:
        for topic, words in enumerate(topics_words):
            gen_word_cloud(topic, ' '.join(words))
            pdf.savefig()
            plt.close()


def gen_word_cloud(title, content):
    plt.figure(figsize=(20, 10))

    wordcloud = WordCloud(
        max_font_size=50,
        max_words=1000,
        background_color='white'
    ).generate(content)

    plt.imshow(wordcloud)
    plt.title(title)
    plt.axis('off')
