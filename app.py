import json
import difflib
from difflib import SequenceMatcher , get_close_matches


data = {}

with open('data.json') as d:
    data = json.load(d)

# print(data['success'])

def check(word):
    for x in data.keys():
        if SequenceMatcher(None, word, x).ratio() > .65:
            ans = input(f"Did you mean {x}?\n").lower()
            if ans == 'yes' or ans == 'y':
                return x
            if ans == 'no' or ans == 'n' :
                return 'none'
        
            


def translate(word):
    print(word)
    word = word.lower()
    index = 0
    if word not in data and word != "\exit":
        correct = check(word)
        if correct == 'none':
            print('No definition available')
        else :
            translate(correct)
    # print(data[word])
    if(word.lower() != '\exit' and word in data):
        for item in data[word]:
            index += 1
            print(f"{index}: {item}\n")

word = ''

while word != '\exit':
    word = input('Select a word or enter "exit" to exit\n')
    translate(word)

if word == '\exit':
    print('Goodbye')
