import requests
from pathlib import Path
import hashlib
import pandas as pd

word_freq = {}
all_guesses = Path('valid-wordle-words.txt').read_text().splitlines()
offensive_words = Path('badwords.txt').read_text().splitlines()
legal_guesses = []


def check_hashes():
    global offensive_words, legal_guesses
    offensive_url = ('https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/badwordslist'
                     '/badwords.txt')
    online = str(requests.get(offensive_url).text.splitlines())
    online_hash = hashlib.sha256(online.encode())
    local_hash = hashlib.sha256(str(offensive_words).encode())
    if local_hash.hexdigest() == online_hash.hexdigest():
        print('Offensive words up-to-date.')
    else:
        offensive_words = list(online)
        print('Offensive words updated.')
    legal_guesses = list(set(all_guesses) - set(offensive_words))


def get_freq():
    freq_list_df = pd.read_csv('unigram_freq.csv', header=0, index_col='word')
    freq_list_df['count'] = freq_list_df['count'].astype(float)
    freq_list = freq_list_df[freq_list_df.index.str.len() == 5]['count'].to_dict()
    for word in legal_guesses:
        word_freq[word] = freq_list.get(word, .1)

    total_freq = sum(word_freq.values())
    for key, value in word_freq.items():
        word_freq[key] = value / total_freq


check_hashes()
get_freq()
# print(word_freq)
