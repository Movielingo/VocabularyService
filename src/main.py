from src.models import MovieGenre
from src.new_movie import extract_save_movie

FILENAME_WORDS_DICT = 'data/cerf_words_dict.pkl'
FILENAME_CONTRACTIONS_DICT = 'data/contractions_dict.pkl'
SUBTITLE_FILE = 'data/half_blood_prince.srt'
MOVIE_TITLE = 'Harry Potter and the Half-Blood Prince'
MOVIE_DESCRIPTION = ("As Harry begins his sixth year at Hogwarts, he discovers an old book marked as 'Property of the "
                     "Half-Blood Prince', and begins to learn more about Lord Voldemort's dark past.")
MOVIE_GENRES = [MovieGenre.FAMILY, MovieGenre.FANTASY]
extract_save_movie(FILENAME_WORDS_DICT, FILENAME_CONTRACTIONS_DICT, SUBTITLE_FILE, MOVIE_DESCRIPTION,
                   MOVIE_GENRES, MOVIE_TITLE)

# FILENAME_WORDS_DICT = 'data/cerf_words_dict.pkl'
# FILENAME_CONTRACTIONS_DICT = 'data/contractions_dict.pkl'
# SUBTITLE_FILE = 'data/chamber_of_secrets.srt'
# MOVIE_TITLE = 'Harry Potter and the Chamber of Secrets'
# MOVIE_DESCRIPTION = (
#     "An ancient prophecy seems to be coming true when a mysterious presence begins stalking the "
#     "corridors of a school of magic and leaving its victims paralyzed.")
# MOVIE_GENRES = [MovieGenre.FAMILY, MovieGenre.FANTASY]
# extract_save_movie(FILENAME_WORDS_DICT, FILENAME_CONTRACTIONS_DICT, SUBTITLE_FILE, MOVIE_DESCRIPTION,
#                    MOVIE_GENRES, MOVIE_TITLE)

# FILENAME_WORDS_DICT = 'data/cerf_words_dict.pkl'
# FILENAME_CONTRACTIONS_DICT = 'data/contractions_dict.pkl'
# SUBTITLE_FILE = 'data/great_gatspy.srt'
# MOVIE_TITLE = 'The Great Gatsby'
# MOVIE_DESCRIPTION = ("A writer and wall street trader, Nick Carraway, finds himself drawn to the past and lifestyle "
#                      "of his mysterious millionaire neighbor, Jay Gatsby, amid the riotous parties of the Jazz Age.")
# MOVIE_GENRES = [MovieGenre.SCIENCE_FICTION, MovieGenre.ROMANCE]
# extract_save_movie(FILENAME_WORDS_DICT, FILENAME_CONTRACTIONS_DICT, SUBTITLE_FILE, MOVIE_DESCRIPTION,
#                    MOVIE_GENRES, MOVIE_TITLE)

# todo oxford cerf list does not contain c2 vocab

# todo better error handling for lemma not found
