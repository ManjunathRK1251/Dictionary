import json,difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def define(word):
    word = word.lower()
    if word in set(data):
        return (word,data[word],True)
    elif len(get_close_matches(word,data.keys(),cutoff=0.8)) > 0:
        inp = input(f"Did you mean {get_close_matches(word,data.keys(),cutoff = 0.8)[0]} instead,if Yes enter Y,else enter N\n")
        if inp.lower() == "y":
            word = get_close_matches(word,data.keys(),cutoff = 0.8)[0]
            return (word,data[word],True)
        elif inp.lower() == "n":
            return (word,"The word "+ word + " doesn't exist in dictionary please double check it", False)
        else:
            return (word,"we didn't understand your entry",False
            )
    else:
        return (word,"The word does not exist,please double check it",False)

while True:
    print("1.Get a definition of word:")
    print("2.Exit")
    print()
    
    try:
        choice = int(input("Enter a choice:"))
        if choice == 1:
            word = input("Enter word:")
            
            word,definition,flag = define(word)
            
            if flag:
                print()
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
        print("2. Please enter a valid Integer")
        print()
