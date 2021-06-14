import mysql.connector
from difflib import get_close_matches   #for finding as many of the most similar words in a dictionary or array by percentage similarity of choice


con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()       #creating a cursor to navigate the database table

# if multiple requests aren't being made to the database for the same values then just get the whole table and process it locally
# query = cursor.execute("SELECT * FROM Dictionary")      #selects all from dictionary table 
# results = cursor.fetchall()                             #data is stored in results as a list of tuples

def to_format(my_str, group=3, char=','):    #to reformat the word with charecters
    my_str = str(my_str)
    my_str = my_str.replace('.', '')
    return char.join(my_str[i:i+group] for i in range(0, (len(my_str)+1), group))


def itsDefinitions(theWord):
    # if multiple requests are being made to the database for the same values and cashing solution for database is available it will be much faster and cheaper
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % theWord)      #selects ,eg: 'inlay', from dictionary table 
    results = cursor.fetchall()
    cursor.reset()
    
    if results: 
        if type(results) == list:     #if there are more than one definitions
            for result in results:   #for each definition in the list
                print(result[1])      #result[0] is the word and result[1] is the meaning in every tuple. Print each, one by one
        else:
            print(results[1])        #if not a list just print the definition. result[0] is the word   
    else:
        theWordAllCaps = theWord.upper()    #capitalize all letters
        theWordAsAbbreviation = to_format(theWordAllCaps, group=1, char='.')     #reformats word as an abreviation
        query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % theWordAsAbbreviation)      #selects ,eg: 'U.S.A.', from dictionary table 
        resultsforAbbreviationForm = cursor.fetchall()
        cursor.reset()
        
        if resultsforAbbreviationForm:
            if type(resultsforAbbreviationForm) == list:     #if there are more than one definitions
                for result in resultsforAbbreviationForm:   #for each definition in the list
                    print(result[1])      #result[0] is the word and result[1] is the meaning in every tuple. Print each, one by one
            else:
                print(results[1])        #if not a list just print the definition. result[0] is the word   
        
        else: 
            print("No word found!")


while True:
    theWord = input("Enter word: ")
    theWord = theWord.lower()       #the inputted word is made lowercase
    theDefinition = itsDefinitions(theWord)     #function is called to find the definitions of the word which can be a list of possible definitions
      
#program does not account for incorrect entries with close matches. For that see the python_EngDictionary repository's engdict.py for json 

#End of Program

