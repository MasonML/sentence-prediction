import os
import re
from training.word_pairs import WordPairs

w_pairs = WordPairs()
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '/../training/datasets/movie_dialogue/movie_lines.txt','r') as f:
    r = f.read()
conversations = r.split("\n")

def clean(s):
    return [i.lower() for i in re.sub('[^A-Za-z0-9 ]+', '', s).split(" ")[8:] if i != '']

for segment in conversations:
    split_segment = segment.split(" ")
    words = clean(segment)
    for w in range(len(words)-1):
        w_pairs.update_tuple_freq(words[w], words[w+1])

print(w_pairs.word_pairs['they'])


