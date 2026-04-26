import requests
import hashlib
from pathlib import Path

url = 'https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/badwordslist/badwords.txt'
r = str(requests.get(url).text.splitlines())
r_hash = hashlib.sha256(r.encode())

local_hash = hashlib.sha256(str(Path('badwords.txt').read_text().splitlines()).encode())
print(local_hash.hexdigest() == r_hash.hexdigest())


