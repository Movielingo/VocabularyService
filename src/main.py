import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from models import MediaGenre, MediaLevel, Series, Episode, MovieInfo
from new_movie import extract_save_media

cred = credentials.Certificate('conf/db_serviceAccount.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'movielingo-717e0.appspot.com'
})

db = firestore.client()

# # Harry potter 6
subtitle_file = 'data/memento.srt'
collection_name = "EnglishMedia"
title = 'Memento'
description = ("It is a 2001 American neo-noir mystery thriller film written and directed by Christopher Nolan. "
               "It stars Guy Pearce, Carrie-Anne Moss, Joe Pantoliano, and Mark Boone Junior.")
genres = [MediaGenre.THRILLER, MediaGenre.ACTION]
level = MediaLevel.ADVANCED
is_series = False
translation_language = "german"
length_min = 113
director = "Christopher Nolan"
release = 2001
media_info = MovieInfo(description=description, is_series=is_series, title=title, genres=genres,
                       level=level, translation_language=[translation_language], length_min=length_min,
                       director=director, release=release, img_ref='data/media/memento.jpeg')
extract_save_media(db, subtitle_file, media_info, collection_name)

# # Harry Potter 2
# subtitle_file = 'data/test.srt'
# collection_name = "EnglishMedia"
#
# title = 'Harry Potter and the Chamber of Secrets'
# description = ("An ancient prophecy seems to be coming true when a mysterious presence begins stalking the "
#                "corridors of a school of magic and leaving its victims paralyzed.")
# genres = [MediaGenre.FAMILY, MediaGenre.FANTASY, MediaGenre.ADVENTURE]
# level = MediaLevel.EASY
# is_series = False
# translation_language = "german"
# length_min = 161
# director = "Chris Columbus"
# release = 2002
# media_info = MovieInfo(description=description, is_series=is_series, title=title, genres=genres,
#                        level=level, translation_language=[translation_language], length_min=length_min,
#                        director=director, release=release, img_ref='data/media/harry_potter_2_english.jpg')
#
# extract_save_media(db, subtitle_file, media_info, collection_name)
#
# # Great Gatsby
# subtitle_file = 'data/test.srt'
# collection_name = "EnglishMedia"
#
# title = 'The Great Gatsby'
# description = ("A writer and wall street trader, Nick Carraway, finds himself drawn to the past and lifestyle "
#                "of his mysterious millionaire neighbor, Jay Gatsby, amid the riotous parties of the Jazz Age.")
# genres = [MediaGenre.SCIENCE_FICTION, MediaGenre.ROMANCE]
# level = MediaLevel.ADVANCED
# is_series = False
# translation_language = "german"
# length_min = 143
# director = "Baz Luhrmann"
# release = 2013
# media_info = MovieInfo(description=description, is_series=is_series, title=title, genres=genres,
#                        level=level, translation_language=[translation_language], length_min=length_min,
#                        director=director, release=release, img_ref='data/media/great_gatsby_english.jpeg')
#
# extract_save_media(db, subtitle_file, media_info, collection_name)

# Friends Season 1 Episode 1
# subtitle_file = 'data/test.srt'
# collection_name = "EnglishMedia"

# title = 'Friends'
# description = """Follows the personal and professional lives of six twenty to thirty year-old friends living in the "
#                "Manhattan borough of New York City."""

# genres = [MediaGenre.COMEDY, MediaGenre.ROMANCE]
# is_series = True
# translation_language = "german"
# release_first_episode = 1994
# release_last_episode = 2005

# episode = 1
# season = 1
# episode_title = "The First One"
# episode_description = """bla bla bla."""

# episode_1 = Episode(episode=episode, season=season, title=episode_title, description=episode_description,
#                     level=MediaLevel.EASY, img_ref='data/media/friends_s1_e2_english.jpeg')

# series = Series(genres=genres, is_series=is_series, title=title, description=description,
#                 release_last_episode=release_last_episode, release_first_episode=release_first_episode,
#                 translation_language=[translation_language], episode_details=episode_1,
#                 img_ref='data/media/friends_english.jpeg')
## adding series including episode
## extract_save_media(db, subtitle_file, series, collection_name)
## adding episode to series
# extract_save_media(db, subtitle_file, episode_1, collection_name, series_ref='SDJ5aLGaQNBUvt2KbMIl')


# TODOS:
# todo oxford cerf list does not contain c2 vocab

# todo better error handling for lemma not found
