import json

data = {}

with open('data.json') as d:
    data = json.load(d)

# print(data['success'])

def translate(word):
    print(data[word])

word = ''

while word != 'exit':
    word = input('Select a word or enter "exit" to exit\n')
    translate(word)

if word == 'exit':
    print('Goodbye')
