import json
import difflib
from difflib import SequenceMatcher     #for the percentage similarity radio of two words
from difflib import get_close_matches   #for finding as many of the most similar words in a dictionary or array by percentage similarity of choice

data = json.load(open("files/engDictionaryData.json"))     #loads a json file. for csv use csv

theSimilarity = SequenceMatcher(None, "rain", "rainn").ratio()      #Finds the similarity ratio, eg: 0.88, that is 88% similarity
print("The similarity between rain and rainn is %.2f" % (theSimilarity*100), "%. Now what word would you like the meaning for?")      #prints the similarity percentage

def to_format(my_str, group=3, char=','):    #to reformat the word with charecters
    my_str = str(my_str)
    return char.join(my_str[i:i+group] for i in range(0, len(my_str), group))

def itsDefinitions(theWord):
    theWordLower = theWord.lower()       #The word is formated to match the dictionary keys. All letters made lowercase. upper for uppercase and title for first letter capitalized
    similarWordsLower = get_close_matches(theWordLower, data.keys())     #for lowercase finds by default 3 words or n=3, with 60% or 0.60 match from keys in dictionary and stores in an array. 

    theWordTitled = theWord.title()       #The word is formated to match the dictionary keys. All letters made titled from delhi to Delhi. upper for uppercase and title for first letter capitalized
    similarWordsTitled = get_close_matches(theWordTitled, data.keys())      #for titled case finds by default 3 words or n=3, with 60% or 0.60 match from keys in dictionary and stores in an array. 

    theWordAllCaps = theWord.upper()       #The word is formated to match the dictionary keys. All letters made uppercase from delhi to Delhi. upper for uppercase and title for first letter capitalized
    similarWordsAllCaps= get_close_matches(theWordAllCaps, data.keys())      #for uppercase finds by default 3 words or n=3, with 60% or 0.60 match from keys in dictionary and stores in an array. 

    theWordAsAbbreviation = to_format(theWord, group=1, char='.')     #reformats word as an abreviation
    similarWordsAsAbbreviation = get_close_matches(theWordAsAbbreviation, data.keys())     #for abreviation finds by default 3 words or n=3, with 60% or 0.60 match from keys in dictionary and stores in an array. 


    similarWordsNotOrdered = similarWordsLower + similarWordsTitled + similarWordsAllCaps + similarWordsAsAbbreviation       #a list of three lists added but not ordered
    similarWordsOrdered = get_close_matches(theWord, similarWordsNotOrdered)     #the list is reordered and refiltered by most similar to least in above 60% match

    
    if theWordLower in data:     #for lowercase checks both the keys and values in dictionary, or values in array or tuple
        return data[theWordLower]        #returns the value to the key in dictionairy

    elif theWordTitled in data:     #for titled case checks both the keys and values in dictionary, or values in array or tuple
        return data[theWordTitled]        #returns the value to the key in dictionairy

    elif theWordAllCaps in data:     #for uppercase checks both the keys and values in dictionary, or values in array or tuple
        return data[theWordAllCaps]        #returns the value to the key in dictionairy

    elif theWordAsAbbreviation in data:     #for if abreviation checks both the keys and values in dictionary, or values in array or tuple
        return data[theWordAsAbbreviation]        #returns the value to the key in dictionairy

    elif  len(similarWordsOrdered) > 0:        #if length of this similarWords array is greater than 1 or if there is atleast 1 word in dictionairy keys that matches the word by atleast 60% or 0.60 then continue, this is the default percent check which can be changed.
        yORn = input("Did you mean %s instead? Enter Y if yes or N if no: " % similarWordsOrdered[0])      #this is the first word in similarWords array. By default get_close_matches gets 3 results from search or n=3, which get stored in an array of heighest percent match to least as long as above 60% match.
        if yORn == "Y":
            return data[similarWordsOrdered[0]]        #returns the value to the first word in similarWords array which is the key of the key value pair in dictionary
        elif yORn == "N":
            return "Sorry. Please double check. Otherwise perhaps there is another word I can help you with today."     #ends current session
        else:
            return "Not a valid input. Lets try this again. Please enter the word you want the meaning for."        #ends current session

    else:
        return "Either not a word or I dont know it. Sorry!"        #ends current session



while True:     #loops infinitely unless manual exit comand on keyboard cntrl+z
    theWord = input("Enter word: ")
    theDefinition = itsDefinitions(theWord)     #function is called to find the definitions of the word which can be a list of possible definitions
    
    if type(theDefinition) == list:     #if there are more than one definitions
        for definitions in theDefinition:   #for each definition in the list
            print(definitions)      #print each, one by one
    else:
        print(theDefinition)        #if not a list just print the definition  


#End of Program



