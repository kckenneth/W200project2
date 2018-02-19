# Homework_06 from Haihui Cao

# This Python script takes a Scrabble rack as a command-line argument and
# prints all valid Scrabble words that can be constructed from that rack,
# along with their Scrabble scores, sorted by score.
# Valid Scrabble words are provided in the file "sowpods.txt"
# A Scrabble rack is made up of any 7 characters.

## Steps:
#1. open SOWPODS.txt and get data list of words
#2. get the command-line argument
#3. construct the rack list using argument and wildcards if any
#4. for each word in rack_list, check the valid words by comparing with data list of words
#5. print out the valid words and their corresponding scores
#6. extra credits. specify the location and specific character and require the arguments big than 3. 

import sys
from score_word import score

#  the official SOWPODS word list constructed as a list named data
with open("sowpods.txt","r") as infile:
    raw_input = infile.readlines()
    data = [datum.strip('\n') for datum in raw_input]
    data = [word for word in data if len(word) <= 7]

# check the argument input. if no argument, print error message and exit.
if len(sys.argv) == 2:
    rack = sys.argv[1].lower()
elif len(sys.argv) >3:
    rack = sys.argv[1].lower()
    loct = int(sys.argv[2])
    charac = sys.argv[3].lower()
else:
    sys.exit("Error: You need to enter some letters without spaces for rack word, an integer for location and letter for the choice")

# construct the rack word list using argument and wildcards if any
number1 = rack.count('*')
number2 = rack.count('?')

rack_split = list(rack)
rack_list = []

if number1 == 0 and number2 == 0:
    rack_list.append(rack)

elif number1 == 1 and number2 == 1 and number1 + number2 < 3:
    for v in 'abcdefghijklmnopqrstuvwxyz':
        rack_word1 = [w.replace('*', v) for w in rack_split]
        for v in 'abcdefghijklmnopqrstuvwxyz':
            rack_word2 = [w.replace('?', v) for w in rack_word1]
            rack_word2.sort()
            rack_word = ''.join(rack_word2)
            rack_list.append(rack_word)
            
elif number1==1 and number1+number2 < 2:
    for v in 'abcdefghijklmnopqrstuvwxyz':
        rack_word1 = [w.replace('*', v) for w in rack_split]
        rack_word1.sort()
        rack_word = ''.join(rack_word1)
        rack_list.append(rack_word)
        
elif number2 == 1 and number1+number2 < 2:
    for v in 'abcdefghijklmnopqrstuvwxyz':
        rack_word1 = [w.replace('?', v) for w in rack_split]
        rack_word1.sort()
        rack_word = ''.join(rack_word1)
        rack_list.append(rack_word)
        
else:
    print("Error: You failed to provide valid wildcards. Wildcards can be either * or ?, and a total of two wild cards at most (one of each character).")


# funtion that counts the letters in a word and return a dictionary
def count_letters(word):
    count = {}
    for letter in word.lower():
        count[letter] = count.get(letter,0) + 1
    return count

# for each word in rack_list, find the valid scrabble words by comparing with data. The valid word is saved in a list.
valid_words = []

# dictionary holding the count_letter list of the word in data if generated 
word_letter_list = {}               

for x in rack_list:
    rack_count = count_letters(x)

    for word in data:
        if set(word.lower()) <= set(x.lower()) and word not in valid_words:
            if word not in word_letter_list.keys():
                letter_lst = {word: count_letters(word)}
                word_letter_list.update(letter_lst)
                word_count = word_letter_list.get(word)
            else:
                word_count = word_letter_list.get(word)
                
            intersec = set(word.lower()).intersection(set(x.lower()))
            letter_number = [(word_count[letter],rack_count[letter]) for letter in intersec]
            if all(item[0] <= item[1] for item in letter_number):
                valid_words.append(word)

# find the score of each valid word, and sort the list. Then print out.
score_list = [(word, score(word)) for word in valid_words]
new_list = sorted(score_list, key=lambda x: x[1], reverse=True)
print(rack.upper(), "-> ", len(new_list), "words,", "Max Score: ", new_list[0][1])
print(new_list)
print()
print()

# Extra credit. If a specific character and location are specified in the arguments, find the corresponding valid words and 
# print out.
if len(sys.argv) >3:
    credit_list = []
    for item in new_list:
        a = list(item[0].lower())
        if len(a) > loct and a[loct] == charac.lower() :
            credit_list.append(item)
    print(rack.upper(), "for location", loct, "with letter", charac, "-> ", len(credit_list), "words")
    print(credit_list)
