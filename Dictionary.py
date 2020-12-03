import json,difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def define(word):
    word = word.lower()
    if word in set(data):
        return (data[word],True)
    elif len(get_close_matches(word,data.keys(),cutoff=0.8)) > 0:
        return (f"Did you mean {get_close_matches(word,data.keys(),cutoff = 0.8)[0]} instead",False)
    else:
        return ("The word does not exist,please double check it",False)

while True:
    print("1.Get a definition of word:")
    print("2.Exit")
    print()
    
    try:
        choice = int(input("Enter a choice:"))
        if choice == 1:
            word = input("Enter word:")
            definition,flag = define(word)
            
            if flag:
                
                print("The definition(s) of " + word + " found in dictonary is/are:")
                print("-"*85)
                for i,w in enumerate(definition):
                    print((str(i+1)+"."),w) 
                print("-"*85)
                print()
            else:
                print(definition)
                print()
        elif choice == 2:
            exit()
        else:
            print("Please enter a valid choice")
            print()
    except ValueError:
        print("Please enter a valid Integer")
        print()
