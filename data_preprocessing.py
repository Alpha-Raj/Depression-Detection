import nltk
import re
from nltk.corpus import stopwords


def preprocess(paragraph):
    # Preprocessing the data
    text = re.sub(r'\[[0-9]*\]', ' ', paragraph)
    text = re.sub(r'\s+', ' ', text)
    text = text.lower()
    text = re.sub(r'\d', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    # Preparing the dataset
    sentences = nltk.sent_tokenize(text)

    sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

    for i in range(len(sentences)):
        sentences[i] = [word for word in sentences[i] if word not in stopwords.words('english')]

    return ' '.join(sentences[0])
