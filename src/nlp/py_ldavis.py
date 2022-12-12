import pyLDAvis
from time import time

from config import settings
from src.utils import format_data_to_pyldavis, save_file
from src.utils.path_utils import make_dir


path = settings.pyldavis_path


def py_ldavis(cleaned_df, tf_model, lda_result, lda_model):
    data = format_data_to_pyldavis(cleaned_df, tf_model, lda_result, lda_model)
    py_lda_prepared_data = pyLDAvis.prepare(**data)
    file_name = f'out-{int(time())}.html'

    make_dir(path)
    save_file('', path, file_name)
    pyLDAvis.save_html(py_lda_prepared_data, f'{path}/{file_name}')
