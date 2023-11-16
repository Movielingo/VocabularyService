from datetime import datetime
from enum import Enum
from typing import List


class VocabSentence:

    def __init__(self, sentence: str, translation: str, timestamp: datetime.time) -> None:
        self.sentence = sentence
        self.translation = translation
        self.timestamp = timestamp

    def to_dict(self):
        dict = self.__dict__
        dict['timestamp'] = str(self.timestamp)
        return dict


class WordLevel(Enum):
    A1 = 'a1'
    A2 = 'a2'
    B1 = 'b1'
    B2 = 'b2'
    C1 = 'c1'
    C2 = 'c2'


class WordType(Enum):
    VERB = 'verb'
    ADV = 'adv'
    NOUN = 'noun'
    ADJ = 'adj'
    ADP = 'adp'
    CCONJ = 'cconj'
    INT = 'int'
    PART = 'part'
    PROPN = 'propn'
    PUNCT = 'punct'
    SCONJ = 'sconj'
    SYM = 'sym'
    DET = 'det'
    PRON = 'pron'
    NUM = 'num'
    AUX = 'aux'
    INTJ = 'intj'
    X = 'x'


class Vocab:

    def __init__(self, lemma: str, word_level: WordLevel, word_type: WordType, sentences: List[VocabSentence],
                 voice_url: str):
        self.lemma = lemma
        self.word_level = word_level
        self.word_type = word_type
        self.sentences = sentences
        self.voice_url = voice_url

    def to_dict(self):
        dict = self.__dict__
        dict['word_level'] = self.word_level.value
        dict['word_type'] = self.word_type.value
        dict['sentences'] = [sentence.to_dict() for sentence in self.sentences]
        return dict


class CSRFWord:

    def __init__(self, word: str, level: WordLevel, pos: str, definition_url: str, voice_url: str):
        self.word = word
        self.level = level
        self.pos = pos
        self.definition_url = definition_url
        self.voice_url = voice_url

    def __repr__(self):
        return f"Word({self.word}, {self.level}, {self.pos}, {self.definition_url}, {self.voice_url})"


class MovieGenre(Enum):
    ACTION = 'action'
    ADVENTURE = 'adventure'
    COMEDY = 'comedy'
    CRIME = 'crime'
    FANTASY = 'fantasy'
    HORROR = 'horror'
    DOCUMENTARY = 'documentary'
    ROMANCE = 'romance'
    SCIENCE_FICTION = 'scienceFiction'
    THRILLER = 'thriller'
    DRAMA = 'drama'
    FAMILY = 'family'


class Movie:
    def __init__(self, description: str, title: str, genres: List[MovieGenre], a1_vocab_count: int, a2_vocab_count: int,
                 b1_vocab_count: int, b2_vocab_count: int, c1_vocab_count: int, c2_vocab_count: int):
        self.description = description
        self.title = title
        self.genres = genres
        self.a1_vocab_count = a1_vocab_count
        self.a2_vocab_count = a2_vocab_count
        self.b1_vocab_count = b1_vocab_count
        self.b2_vocab_count = b2_vocab_count
        self.c1_vocab_count = c1_vocab_count
        self.c2_vocab_count = c2_vocab_count

    def to_dict(self):
        dict = self.__dict__
        genres = []
        for genre in self.genres:
            genres.append(genre.value)
        dict['genres'] = genres
        return dict
