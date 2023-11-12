import firebase_admin
import spacy
from firebase_admin import credentials
from firebase_admin import firestore

from src.models import Movie, WordLevel
from src.subtitle_words import extract_unique_words_subtitles
from src.word_level_contractions import load_dict


def _get_movie_dict(MOVIE_DESCRIPTION, MOVIE_GENRES, MOVIE_TITLE, vocab_dict):
    return Movie(description=MOVIE_DESCRIPTION, genres=MOVIE_GENRES, title=MOVIE_TITLE,
                 a1_vocab_count=len(vocab_dict[WordLevel.A1.value]), a2_vocab_count=len(vocab_dict[WordLevel.A2.value]),
                 b1_vocab_count=len(vocab_dict[WordLevel.B1.value]), b2_vocab_count=len(vocab_dict[WordLevel.B2.value]),
                 c1_vocab_count=len(vocab_dict[WordLevel.C1.value]),
                 c2_vocab_count=len(vocab_dict[WordLevel.C2.value])).to_dict()


def _get_vocab_all_levels(vocab_dict):
    vocab_dict_all_levels = {}
    vocab_dict_all_levels.update(vocab_dict['a1'])
    vocab_dict_all_levels.update(vocab_dict['a2'])
    vocab_dict_all_levels.update(vocab_dict['b1'])
    vocab_dict_all_levels.update(vocab_dict['b2'])
    vocab_dict_all_levels.update(vocab_dict['c1'])
    vocab_dict_all_levels.update(vocab_dict['c2'])
    return vocab_dict_all_levels


def _vocab_batch_write(vocab_dict_all_levels, new_movie_ref, db):
    batch = db.batch()
    batch_size = 0
    vocab_collection_ref = new_movie_ref[1].collection('vocabulary')

    for vocab_key, vocab_value in vocab_dict_all_levels.items():
        if batch_size == 500:
            batch.commit()
            batch = db.batch()
            batch_size = 0

        doc_ref = vocab_collection_ref.document()
        batch.set(doc_ref, vocab_value.to_dict())
        batch_size += 1

    if batch_size > 0:
        batch.commit()
    print('Done saving vocabulary.')


def extract_save_movie(FILENAME_WORDS_DICT, FILENAME_CONTRACTIONS_DICT, SUBTITLE_FILE, MOVIE_DESCRIPTION,
                       MOVIE_GENRES, MOVIE_TITLE):
    cred = credentials.Certificate('data/db_serviceAccount.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    nlp = spacy.load("en_core_web_sm")

    csrf_words = load_dict(FILENAME_WORDS_DICT)
    formal_contractions = load_dict(FILENAME_CONTRACTIONS_DICT)

    vocab_dict = extract_unique_words_subtitles(SUBTITLE_FILE, csrf_words, nlp, formal_contractions)
    print('Done extracting vocab from subtitle file.')

    movie_dict = _get_movie_dict(MOVIE_DESCRIPTION, MOVIE_GENRES, MOVIE_TITLE, vocab_dict)

    new_movie_ref = db.collection('movies').add(movie_dict)
    print(f'Created new document for movie with ref: {new_movie_ref[0].id}')
    vocab_dict_all_levels = _get_vocab_all_levels(vocab_dict)
    _vocab_batch_write(vocab_dict_all_levels, new_movie_ref, db)
