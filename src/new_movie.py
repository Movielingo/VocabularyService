from src.main import extract_save_movie
from src.models import MovieGenre

FILENAME_WORDS_DICT = 'data/cerf-words-dict.pkl'
FILENAME_CONTRACTIONS_DICT = 'data/contractions-dict.pkl'
SUBTITLE_FILE = 'data/harry_potter.srt'
MOVIE_TITLE = 'Harry Potter and the Half-Blood Prince'
MOVIE_DESCRIPTION = ("As Harry begins his sixth year at Hogwarts, he discovers an old book marked as 'Property of the "
                     "Half-Blood Prince', and begins to learn more about Lord Voldemort's dark past.")
MOVIE_GENRES = [MovieGenre.FAMILY, MovieGenre.FANTASY]

extract_save_movie(FILENAME_WORDS_DICT, FILENAME_CONTRACTIONS_DICT, SUBTITLE_FILE, MOVIE_DESCRIPTION,
                   MOVIE_GENRES, MOVIE_TITLE)

# todo oxford cerf list does not contain c2 vocab
