from fnmatch import translate
from difflib import get_close_matches
import json

from matplotlib.font_manager import json_load
from numpy import outer
f = open('data.json')
data = json.load(f)
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0: 
        print("did you mean %s instead"%get_close_matches(word,data.keys())[0])
        decide = input("Press y for yes or n for no : ")
        if decide == "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif decide == "n":
            return["You have enter wrong key "]
        else:
            return["You have enter wrong input please input y or n"]      

    else:
        print("You have enter wrong word ")    

word = input("Enter the word you want to search : ")
output = translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:        
    print(output)
