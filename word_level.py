import csv
import pickle

FILENAME_WORDS_DICT = 'cerf-words-dict.pkl'


class Word:
    def __init__(self, word, level, pos, definition_url, voice_url):
        self.word = word
        self.level = level
        self.pos = pos
        self.definition_url = definition_url
        self.voice_url = voice_url

    def __repr__(self):
        return f"Word({self.word}, {self.level}, {self.pos}, {self.definition_url}, {self.voice_url})"


def extract_words_from_csv(file_path):
    words_dict = {}
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            word_obj = Word(row[0], row[1], row[2], row[3], row[4])
            words_dict[row[0]] = word_obj
    return words_dict


def save_words_dict(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


def load_words_dict(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)


def get_word_cerf_level(word: str) -> [Word, None]:
    words_dict = load_words_dict(FILENAME_WORDS_DICT)
    word = word.lower()
    try:
        return words_dict[word]
    except KeyError:
        return None

# words_dict_from_csv = extract_words_from_csv("oxford-5k.csv")

# save_words_dict(words_dict_from_csv, filename_words_dict)
