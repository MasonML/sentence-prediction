import os
import re
from prediction.dictionary import Dictionary

dictionary = Dictionary()
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '/../datasets/movie_dialogue/movie_lines.txt','r') as f:
    r = f.read()
conversations = r.split("\n")

def clean(s):
    return [i.lower() for i in re.sub('[^A-Za-z0-9 ]+', '', s).split(" ")[8:] if i != '']

for segment in conversations:
    split_segment = segment.split(" ")
    words = clean(segment)
    for w in range(len(words)-1):
        dictionary.update_tuple_freq(words[w], words[w+1])

print(dictionary.word_pairs['they'])


