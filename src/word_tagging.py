from models import WordType


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
        print(f'lemma not found {word}: {sentence}')
        # raise ValueError('Lemma not found!') #todo error handling
        return None, None
    return lemma, WordType[word_type]
