import json
from difflib import get_close_matches

#Dictionary words and defs json file
words = json.load(open("source/data.json"))

#Function returns definitions
def define(w):
    # w = w.lower() another way to ensure word case is the same
    if w in words:
        return words[w]
    elif w.title() in words:
        return words[w.title()]
    elif len(get_close_matches(w, words.keys())) > 0:
        yn = input("Did you possibley mean \"%s\" instead?  Enter 'Y' or 'N' " % get_close_matches(w, words.keys())[0])
        if yn == "Y":
            return words[get_close_matches(w, words.keys())[0]]
        elif yn == "N":
            return "The word does not exist try again"
        else:
            return "We didn't understand your entry"
    else:
        return "The word does not exist try again"

word = input("Enter a word: ").lower()

output = (define(word))

if type(output) == list:
    for item in output:
        print (item)
else:
    print (output)
