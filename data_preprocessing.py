import re 

from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords
from bs4 import BeautifulSoup


__word_punct_tokenizer = WordPunctTokenizer()
__stop_words = stopwords.words('english')


def remove_html_tags(html):
    return BeautifulSoup(html).get_text()


def stay_only_a_z(text):
    text = re.sub(r'[^a-zA-Z\s]','', text)
    return text


def tokenize_by_word(text):
    return ' '.join(__word_punct_tokenizer.tokenize(text))


def remove_stop_words(text):
    return ' '.join([word for word in text.split() if word.lower() not in __stop_words])
