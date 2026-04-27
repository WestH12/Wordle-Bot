import requests
from pathlib import Path
import hashlib
import pandas as pd
import math

word_freq = {}
all_guesses = Path('files/valid-wordle-words.txt').read_text().splitlines()
offensive_words = Path('files/badwords.txt').read_text().splitlines()
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
    freq_list_df = pd.read_csv('files/unigram_freq.csv', header=0, index_col='word')
    freq_list_df['count'] = freq_list_df['count'].astype(float)
    freq_list = freq_list_df[freq_list_df.index.str.len() == 5]['count'].to_dict()
    for word in legal_guesses:
        word_freq[word] = freq_list.get(word, min(freq_list.values()))

    log_freq = {word: math.log(freq) for word, freq in word_freq.items()}
    min_log = min(log_freq.values())
    max_log = max(log_freq.values())
    epsilon = 1e-4
    for word in log_freq:
        normalized = (log_freq[word] - min_log) / (max_log - min_log)

        word_freq[word] = epsilon + (1 + epsilon) * normalized


check_hashes()
get_freq()
print(max(word_freq.values()))
