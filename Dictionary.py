import json
data = json.load(open("data.json"))

def define(word):
    if word.lower() in set(data):
        return data[word.lower()]
    else:
        return "The word does not exist,please double check it"

word = input("Enter word:")

print("The definition(s) of " + word + " found in dictonary is/are:")
for i,w in enumerate(define(word)):
    print((str(i+1)+"."),w)