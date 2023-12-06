from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List


@dataclass
class VocabSentence:
    sentence: str
    translation: str
    timestamp: datetime.time

    def to_dict(self):
        data = self.__dict__
        data['timestamp'] = str(self.timestamp)
        return data


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


@dataclass
class Vocab:
    lemma: str
    word_level: WordLevel
    word_type: WordType
    sentences: List[VocabSentence]
    voice_url: str
    translationLanguage: str

    def to_dict(self):
        data = self.__dict__
        data['word_level'] = self.word_level.value
        data['word_type'] = self.word_type.value
        data['sentences'] = [sentence.to_dict() for sentence in self.sentences]
        return data


@dataclass
class CSRFWord:
    word: str
    level: WordLevel
    pos: str
    definition_url: str
    voice_url: str

    def __repr__(self):
        return f"Word({self.word}, {self.level}, {self.pos}, {self.definition_url}, {self.voice_url})"


class MediaGenre(Enum):
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


class MediaLevel(Enum):
    HARD = 'hard'
    EASY = 'easy'
    ADVANCED = 'advanced'


@dataclass
class MediaInfo:
    description: str
    is_series: bool
    title: str
    genres: List[MediaGenre]
    translation_language: [str]
    img_ref: str


@dataclass
class MovieInfo(MediaInfo):
    level: MediaLevel
    length_min: int
    director: str
    release: int


@dataclass
class Episode:
    episode: int
    title: str
    description: str
    level: MediaLevel
    season: int
    img_ref: str
    a1_vocab_count: int = 0
    a2_vocab_count: int = 0
    b1_vocab_count: int = 0
    b2_vocab_count: int = 0
    c1_vocab_count: int = 0
    c2_vocab_count: int = 0

    def to_dict(self):
        data = self.__dict__
        data['level'] = self.level.value
        return data

    def add_vocab_count_to_episode(self, vocab_dict: dict):
        self.a1_vocab_count = len(vocab_dict[WordLevel.A1.value])
        self.a2_vocab_count = len(vocab_dict[WordLevel.A2.value])
        self.b1_vocab_count = len(vocab_dict[WordLevel.B1.value])
        self.b2_vocab_count = len(vocab_dict[WordLevel.B2.value])
        self.c1_vocab_count = len(vocab_dict[WordLevel.C1.value])
        self.c2_vocab_count = len(vocab_dict[WordLevel.C2.value])


@dataclass
class Series(MediaInfo):
    episode_details: Episode
    release_first_episode: int
    release_last_episode: int

    def to_dict(self):
        data = self.__dict__
        genres = []
        for genre in self.genres:
            genres.append(genre.value)
        data['genres'] = genres
        data['episode_details'] = [self.episode_details.to_dict()]
        return data

    def add_vocab_count_to_episode(self, vocab_dict: dict):
        self.episode_details.a1_vocab_count = len(vocab_dict[WordLevel.A1.value])
        self.episode_details.a2_vocab_count = len(vocab_dict[WordLevel.A2.value])
        self.episode_details.b1_vocab_count = len(vocab_dict[WordLevel.B1.value])
        self.episode_details.b2_vocab_count = len(vocab_dict[WordLevel.B2.value])
        self.episode_details.c1_vocab_count = len(vocab_dict[WordLevel.C1.value])
        self.episode_details.c2_vocab_count = len(vocab_dict[WordLevel.C2.value])


@dataclass
class Movie(MovieInfo):
    a1_vocab_count: int
    a2_vocab_count: int
    b1_vocab_count: int
    b2_vocab_count: int
    c1_vocab_count: int
    c2_vocab_count: int

    def to_dict(self):
        data = self.__dict__
        genres = []
        for genre in self.genres:
            genres.append(genre.value)
        data['genres'] = genres
        data['level'] = self.level.value
        return data

    @classmethod
    def get_movie_dict(cls, media_info: MediaInfo, vocab_dict: dict):
        return Movie(description=media_info.description, genres=media_info.genres, title=media_info.title,
                     level=media_info.level, is_series=media_info.is_series,
                     translation_language=media_info.translation_language, length_min=media_info.length_min,
                     director=media_info.director, release=media_info.release, img_ref=media_info.img_ref,
                     a1_vocab_count=len(vocab_dict[WordLevel.A1.value]),
                     a2_vocab_count=len(vocab_dict[WordLevel.A2.value]),
                     b1_vocab_count=len(vocab_dict[WordLevel.B1.value]),
                     b2_vocab_count=len(vocab_dict[WordLevel.B2.value]),
                     c1_vocab_count=len(vocab_dict[WordLevel.C1.value]),
                     c2_vocab_count=len(vocab_dict[WordLevel.C2.value]))
