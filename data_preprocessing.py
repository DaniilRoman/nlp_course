import re 

from nltk.tokenize import WordPunctTokenizer
from bs4 import BeautifulSoup


__word_punct_tokenizer = WordPunctTokenizer()


def remove_html_tags(html):
    return BeautifulSoup(html).get_text()


def stay_only_a_z(text):
    text = re.sub(r'[^(a-zA-Z)\s]','', text)
    return text


def tokenize_by_word(text):
    return ' '.join(__word_punct_tokenizer.tokenize(text))
