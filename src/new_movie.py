import firebase_admin
import spacy
from firebase_admin import credentials
from firebase_admin import firestore

from src.db_service import save_movie_to_db, save_series_to_db, vocab_batch_write, save_episode_to_db, \
    upload_image_to_storage
from src.models import MediaInfo, MovieInfo, Series, Episode
from src.subtitle_words import extract_unique_words_subtitles
from src.word_level_contractions import load_csrf_dict, load_contractions_dict


def _get_vocab_all_levels(vocab_dict):
    vocab_dict_all_levels = {}
    vocab_dict_all_levels.update(vocab_dict['a1'])
    vocab_dict_all_levels.update(vocab_dict['a2'])
    vocab_dict_all_levels.update(vocab_dict['b1'])
    vocab_dict_all_levels.update(vocab_dict['b2'])
    vocab_dict_all_levels.update(vocab_dict['c1'])
    vocab_dict_all_levels.update(vocab_dict['c2'])
    return vocab_dict_all_levels


def extract_save_media(subtitle_file, media_info: [MediaInfo, Episode], collection_name: str, series_ref: str = None):
    cred = credentials.Certificate('conf/db_serviceAccount.json')
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'movielingo-717e0.appspot.com'
    })

    db = firestore.client()
    nlp = spacy.load("en_core_web_sm")
    episode = None
    season = None
    csrf_words = load_csrf_dict()
    formal_contractions = load_contractions_dict()

    vocab_dict = extract_unique_words_subtitles(subtitle_file, csrf_words, nlp, formal_contractions)
    print('Done extracting vocab from subtitle file.')
    img_ref = upload_image_to_storage(media_info.img_ref)
    if isinstance(media_info, MovieInfo):
        media_ref = save_movie_to_db(media_info, collection_name, vocab_dict, img_ref, db)

    elif isinstance(media_info, Series):
        episode = media_info.episode_details.episode
        season = media_info.episode_details.season
        media_ref = save_series_to_db(media_info, collection_name, vocab_dict, img_ref, db)
    elif isinstance(media_info, Episode):
        episode = media_info.episode
        season = media_info.season
        media_ref = save_episode_to_db(media_info, series_ref, collection_name, vocab_dict, img_ref, db)

    else:
        raise Exception('MediaInfo type not supported.')
    print(f'Created new document for movie with ref: {media_ref.id}')
    vocab_dict_all_levels = _get_vocab_all_levels(vocab_dict)

    vocab_batch_write(vocab_dict_all_levels, media_ref, db, season, episode)
