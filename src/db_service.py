from firebase_admin import storage
from google.cloud.firestore import ArrayUnion, DocumentReference

from src.models import Movie, MovieInfo, Series, Episode


def _snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


def _convert_keys_to_camel_case(obj):
    if isinstance(obj, dict):
        new_dict = {}
        for key, value in obj.items():
            new_key = _snake_to_camel(key)
            new_dict[new_key] = _convert_keys_to_camel_case(value)
        return new_dict
    elif isinstance(obj, list):
        return [_convert_keys_to_camel_case(item) for item in obj]
    else:
        return obj


def _string_to_trigrams(media_title: str) -> dict[str, bool]:
    media_title = media_title.lower()
    trigrams = {}
    for i in range(len(media_title) - 2):
        trigram = media_title[i:i + 3]
        trigrams[trigram] = True
    return trigrams


def _add_trigrams_to_media(media_dict: dict) -> dict:
    trigrams = _string_to_trigrams(media_dict['title'])
    for trigram in trigrams:
        media_dict[trigram] = True
    return media_dict


def save_movie_to_db(media_info: MovieInfo, collection_name: str, vocab_dict: dict, img_ref: str,
                     db) -> DocumentReference:
    movie_dict = Movie.get_movie_dict(media_info, vocab_dict).to_dict()
    movie_dict = _add_trigrams_to_media(movie_dict)
    movie_dict_camel_case = _convert_keys_to_camel_case(movie_dict)
    movie_dict_camel_case['imgRef'] = img_ref

    new_movie_ref = db.collection(collection_name).add(movie_dict_camel_case)
    return new_movie_ref[1]


def save_series_to_db(series: Series, collection_name: str, vocab_dict: dict, img_ref: str, db) -> DocumentReference:
    series.add_vocab_count_to_episode(vocab_dict)
    series_dict = series.to_dict()
    series_dict = _add_trigrams_to_media(series_dict)
    series_dict_camel_case = _convert_keys_to_camel_case(series_dict)
    series_dict_camel_case['imgRef'] = img_ref
    new_series_ref = db.collection(collection_name).add(series_dict_camel_case)
    return new_series_ref[1]


def save_episode_to_db(episode: Episode, series_id: str, collection_name: str, vocab_dict: dict, img_ref: str,
                       db) -> DocumentReference:
    episode.add_vocab_count_to_episode(vocab_dict)
    episode_dict = episode.to_dict()
    episode_dict_camel_case = _convert_keys_to_camel_case(episode_dict)
    episode_dict_camel_case['imgRef'] = img_ref
    series_ref = db.collection(collection_name).document(series_id)
    series_ref.update({
        'episodeDetails': ArrayUnion([episode_dict_camel_case])
    })
    return series_ref


def vocab_batch_write(vocab_dict_all_levels, new_media_ref, db, series: int = None, episode: int = None):
    batch = db.batch()
    batch_size = 0
    vocab_collection_ref = new_media_ref.collection('Vocabularies')

    for vocab_key, vocab_value in vocab_dict_all_levels.items():
        if batch_size == 500:
            batch.commit()
            batch = db.batch()
            batch_size = 0

        doc_ref = vocab_collection_ref.document()
        vocab_dict = _convert_keys_to_camel_case(vocab_value.to_dict())
        if series and episode:
            vocab_dict['series'] = series
            vocab_dict['episode'] = episode
        batch.set(doc_ref, vocab_dict)
        batch_size += 1

    if batch_size > 0:
        batch.commit()
    print('Done saving vocabulary.')


def upload_image_to_storage(image_path):
    blob_name = f'media/{image_path.split("/")[-1]}'
    bucket = storage.bucket()
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(image_path)
    return blob_name
