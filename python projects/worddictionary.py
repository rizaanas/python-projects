'''
def main():
    word_dictionary = {
    'hi':'a way of greeting',
    'eyes' : 'an organ for seeing',
    'earth': 'a planet in space',
    }


    while True:
        word = input ("enter a word : ")
        if word == "":
            break
        if word in word_dictionary:
            print (word,":",word_dictionary[word])

main()
'''

'''
from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = input ("Enter your word: ")
    if word == "":
        break
    print(dictionary.meaning(word))
'''


'''
from PyDictionary import PyDictionary

dictionary = PyDictionary("eyes","head","cat")

print(dictionary.printMeanings())
'''

'''
from PyDictionary import PyDictionary

dictionary = PyDictionary("love","one","riza")

print(dictionary.getMeanings())
'''



