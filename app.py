import json

data = {}

with open('data.json') as d:
    data = json.load(d)

# print(data['success'])

def translate(word):
    word = word.lower()
    index = 0
    if word not in data:
        print('No definition available')
    # print(data[word])
    if(word.lower() != 'exit' and word in data):
        for item in data[word]:
            index += 1
            print(f"{index}: {item}\n")

word = ''

while word != 'exit':
    word = input('Select a word or enter "exit" to exit\n')
    translate(word)

if word == 'exit':
    print('Goodbye')
