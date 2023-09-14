import re


def extract_unique_words_subtitles(srt_file_path):
    unique_words = set()
    excluded_words = {"harry", "potter"}
    with open(srt_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        # Skip sequence numbers, timestamps, and empty lines
        if re.match(r"^\d+$", line.strip()) or \
                re.match(r"^\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}$", line.strip()) or \
                line.strip() == "":
            continue

        # Extract words, convert to lowercase, and add to set (if not in excluded_words)
        words = [word.lower() for word in re.findall(r"\b\w+\b", line) if word.lower() not in excluded_words]
        unique_words.update(words)

    return unique_words


subtitle_words = extract_unique_words_subtitles('harry_potter.srt')

"""
extract unique words from pdf files
convert words into 'grundform', add workd classification => spacy
classify word into cerf level
get context translation
store word in db
"""
