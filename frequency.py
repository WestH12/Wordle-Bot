import requests

word_freq = {}

def get_freq(word):
    # Creates the url to call the datamuse api with the desired word
    url =  "https://api.datamuse.com/words?sp=" + word+"&md=f&max=1"
    payload = requests.get(url).json() #Captures the payload from the api call
    # Indexes the word frequency, converts it to a float, and adds it to the global frequency list
    word_freq[word] = float(payload[0]['tags'][0][2:])

get_freq('power')
print(word_freq.get('power'))
