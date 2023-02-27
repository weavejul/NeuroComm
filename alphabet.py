import re
from collections import Counter

# Import txt file, make lowercase, remove non-alphabetic characters.
worldFactbook = open('worldFactbook.txt', 'r')
txtContent = re.sub(r'[^a-z]', '', worldFactbook.read().lower())
letterFreqs = Counter(txtContent)

worldFactbook.close()