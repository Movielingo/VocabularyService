import spacy

nlp = spacy.load("en_core_web_sm")


def get_lemma_and_pos(word) -> [str, str]:
    doc = nlp(word)
    token = doc[0]  # Assuming a single word is provided
    return token.lemma_, token.pos_

# lemma, pos = get_lemma_and_pos("walked")
