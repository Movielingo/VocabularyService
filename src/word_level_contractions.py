import csv
import pickle

from models import CSRFWord, WordLevel, WordType


def extract_words_from_csv(file_path):
    words_dict = {}
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            word_obj = CSRFWord(word=row[0], level=WordLevel(row[1]), pos=WordType(row[2]), definition_url=row[3],
                                voice_url=row[4])
            words_dict[row[0]] = word_obj
    return words_dict


def save_words_dict(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


def load_dict(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)


def get_word_cerf_level(word: str, csrf_words: dict) -> [CSRFWord, None]:
    word = word.lower()
    try:
        return csrf_words[word]
    except KeyError:
        return None


def create_constractions_dict(filename: str):
    dict = {}
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row == ['', '']:
                break
            else:
                dict[row[0]] = row[1]
    save_words_dict(dict, 'data/contractions-dict.pkl')


# get_word_cerf_level('I')

# words_dict_from_csv = extract_words_from_csv("oxford-5k.csv")

create_constractions_dict('data/informal_contractions.csv')
# save_words_dict(words_dict_from_csv, FILENAME_WORDS_DICT)
