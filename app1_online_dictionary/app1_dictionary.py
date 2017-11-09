import json

from difflib import get_close_matches


words = json.load(open("source/data.json"))

def define(w):
    # w = w.lower() another way to ensure word case is the same
    if w in words:
        return words[w]
    elif len(get_close_matches(w, words.keys(), cutoff=.9)) > 0:
        return "Did you possibley mean \"%s\" instead? " % get_close_matches(w, words.keys())[0]
    else:
        return "The word does not exist try again"

word = input("Enter a word: ").lower()

print (define(word))
