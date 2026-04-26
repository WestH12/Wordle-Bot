import requests
from pathlib import Path

word_freq = {}
all_guesses = Path('valid-wordle-words.txt').read_text().splitlines()
offensive_words = Path('badwords.txt').read_text().splitlines()
#TODO: Add hash check to ensure up to date offensive words txt file
legal_guesses = list(set(all_guesses) - set(offensive_words))

def get_freq(word):
    # Creates the url to call the datamuse api with the desired word
    url =  "https://api.datamuse.com/words?sp=" + word+"&md=f&max=1"
    payload = requests.get(url).json() #Captures the payload from the api call
    # Indexes the word frequency, converts it to a float, and adds it to the global frequency list
    word_freq[word] = float(payload[0]['tags'][0][2:])

def get_all_freq(guess_list):
    for i in range(len(guess_list)):
        get_freq(guess_list[i])

    total_freq = sum(word_freq.values())
    for key, value in word_freq.items():
        word_freq[key] = value / total_freq


