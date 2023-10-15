import firebase_admin
import spacy
from firebase_admin import credentials
from firebase_admin import firestore

from src.models import MovieGenre, Movie, WordLevel
from src.subtitle_words import extract_unique_words_subtitles
from src.word_level import load_dict

# todo oxford cerf list does not contain c2 vocab
FILENAME_WORDS_DICT = 'data/cerf-words-dict.pkl'
FILENAME_CONTRACTIONS_DICT = 'data/contractions-dict.pkl'
SUBTITLE_FILE = 'data/harry_potter.srt'
MOVIE_TITLE = 'Harry Potter and the Half-Blood Prince'
MOVIE_DESCRIPTION = ("As Harry begins his sixth year at Hogwarts, he discovers an old book marked as 'Property of the "
                     "Half-Blood Prince', and begins to learn more about Lord Voldemort's dark past.")
MOVIE_GENRES = [MovieGenre.FAMILY, MovieGenre.FANTASY]

# Use a service account.
cred = credentials.Certificate('data/db_serviceAccount.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
nlp = spacy.load("en_core_web_sm")

csrf_words = load_dict(FILENAME_WORDS_DICT)
formal_contractions = load_dict(FILENAME_CONTRACTIONS_DICT)

vocab_dict = extract_unique_words_subtitles(SUBTITLE_FILE, csrf_words, nlp, formal_contractions)
print('done extracting')

movie_collection_ref = db.collection('movies')
movie = Movie(description=MOVIE_DESCRIPTION, genres=MOVIE_GENRES, title=MOVIE_TITLE,
              a1_vocab_count=len(vocab_dict[WordLevel.A1.value]), a2_vocab_count=len(vocab_dict[WordLevel.A2.value]),
              b1_vocab_count=len(vocab_dict[WordLevel.B1.value]), b2_vocab_count=len(vocab_dict[WordLevel.B2.value]),
              c1_vocab_count=len(vocab_dict[WordLevel.C1.value]), c2_vocab_count=len(vocab_dict[WordLevel.C2.value]))
movie_dict = movie.to_dict()
new_movie_ref = db.collection('movies').add(movie_dict)
new_movie_id = new_movie_ref[1].id
vocab_a1_collection_ref = movie_collection_ref.document(new_movie_id).collection('a1Vocabulary')
for entry in vocab_dict[WordLevel.A1.value]:
    vocab_a1_collection_ref.add(vocab_dict[WordLevel.A1.value][entry].to_dict())
