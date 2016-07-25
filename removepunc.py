__author__ = 'Hernan Y.Ke'
import string

sonnets = open("sonnet.txt").readlines()
word_set = set([elt.strip() for elt in open("pod.txt")])
sonnet_words = set()

def strip_punc(word):
    word.replace("-"," ")
    apostrophe_idx = word.find("'")
    if apostrophe_idx != -1:
        return None
    return word.strip(string.punctuation)
for line in sonnets:
    line_words = line.replace("-"," ").strip().split()
    if len(line_words)<=1:
        continue
    for word in line_words:
        stripped = strip_punc(word)
        if stripped and len(stripped)>1:
            sonnet_words.add(stripped.upper())
sonnet_words=list(sonnet_words)
sonnet_words.sort()

f = open("sonword.txt","w")
for word in sonnet_words:
    f.write(word+"\n")
f.close()