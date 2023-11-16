from src.models import WordType


def get_lemma(sentence, word, nlp):
    doc = nlp(sentence)
    lemma = None
    word_type = None
    for token in doc:
        if token.text == word:
            lemma = token.lemma_
            word_type = token.pos_
            break
    if not lemma:
        raise ValueError('Lemma not found!')
    return lemma, WordType[word_type]
