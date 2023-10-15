import re
from datetime import datetime

from models import VocabSentence, Vocab
from translation import translate_to_german
from word_level import get_word_cerf_level
from word_tagging import get_lemma


def get_tiemstamp(match: re.Match) -> datetime.time:
    hour_min_s = match.group(1).split(',')[0]
    return datetime.strptime(hour_min_s, '%H:%M:%S').time()


def filter_words(line: str, inf_contractions) -> []:
    excluded_words = {"harry", "potter", "mr", "ms", "mrs", "o", "w", "l", "", "\n", " ", "!", ".", "?", ",", '"'}
    words = re.findall(r"(\w+'\w+|\w+|\W)", line)
    filtered_words = []
    for idx, word in enumerate(words):
        if word.lower() in excluded_words:
            continue
        if len(word) == 1:
            continue
        if "'" in word:
            # todo deal with abbreviations like isn't
            continue
        # todo deal with informal contractions
        if word in inf_contractions:
            continue
        filtered_words.append(word)
    return filtered_words


def extract_vocab(unique_words, sentence, timestamp, csrf_words, nlp, inf_contractions):
    sentence = sentence.replace('\n', '')
    translation = translate_to_german(sentence)
    vocab_sentence = VocabSentence(sentence, translation, timestamp)

    words = filter_words(sentence, inf_contractions)

    for word in words:
        lemma, word_type = get_lemma(sentence, word, nlp)

        # todo check if csrf word type and spicy word type match
        csrf_word = get_word_cerf_level(lemma, csrf_words)
        if not csrf_word:
            continue
        if lemma in unique_words[csrf_word.level.value]:
            unique_words[csrf_word.level.value][lemma].sentences.append(vocab_sentence)
        unique_words[csrf_word.level.value][lemma] = Vocab(lemma=lemma, word_type=word_type, word_level=csrf_word.level,
                                                           sentences=[vocab_sentence], voice_url=csrf_word.voice_url)
    return unique_words


def extract_unique_words_subtitles(srt_file_path, csrf_words, nlp, inf_contractions):
    unique_words = {'a1': {}, 'a2': {}, 'b1': {}, 'b2': {}, 'c1': {}, 'c2': {}}

    timestamp = None
    with open(srt_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    timestamp_re = re.compile(r'(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})')
    skip = False
    for idx, line in enumerate(lines):
        print(f'Line: {idx}')

        if skip:
            skip = False
            continue
        match = timestamp_re.search(line)
        if match:
            timestamp = get_tiemstamp(match)
            skip = False
        elif re.match(r"^\d+$", line.strip()) or \
                re.match(r"^\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}$", line.strip()) or \
                line.strip() == "":
            skip = False
            continue
        else:

            sentence = line

            if lines[idx + 1] is not '\n':
                sentence += " " + lines[idx + 1]
                skip = True
            unique_words = extract_vocab(unique_words, sentence, timestamp, csrf_words, nlp, inf_contractions)

    return unique_words
