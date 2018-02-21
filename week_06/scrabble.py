# Homework_06 from Haihui Cao

# This Python script takes a Scrabble rack as a command-line argument and
# prints all valid Scrabble words that can be constructed from that rack,
# along with their Scrabble scores, sorted by score.
# Valid Scrabble words are provided in the file "sowpods.txt"
# A Scrabble rack is made up of any 7 characters.

import sys
from score_word import score

#  the official SOWPODS word list constructed as a list named data
with open("sowpods.txt","r") as infile:
    raw_input = infile.readlines()
    data = [datum.strip('\n') for datum in raw_input]
    data = [word for word in data if len(word)<=7]
# check the argument input. if no argument, print error message and exit.

if len(sys.argv) >= 2:
    rack = sys.argv[1].lower()
    loc = sys.argv[2]
else:
    sys.exit("Error: You need to enter some letters without spaces")

number1 = rack.count('*')
number2 = rack.count('?')
rack_split=list(rack)
rack_list=[]

if number1 ==0 and number2==0:
    rack_list.append(rack)

elif number1==1 and number2==1 and number1+number2 < 3:
    for v in 'abcdefghijklmnopqrstuvwxyz':
        rack_word1 = [w.replace('*', v) for w in rack_split]
        for v in 'abcdefghijklmnopqrstuvwxyz':
            rack_word2 = [w.replace('?', v) for w in rack_word1]
            rack_word=''.join(rack_word2)
            rack_list.append(rack_word)
elif number1==1 and number1+number2 < 2:
    for v in 'abcdefghijklmnopqrstuvwxyz':
        rack_word1 = [w.replace('*', v) for w in rack_split]
        rack_word=''.join(rack_word1)
        rack_list.append(rack_word)
elif number2==1 and number1+number2 < 2:
    for v in 'abcdefghijklmnopqrstuvwxyz':
        rack_word1 = [w.replace('?', v) for w in rack_split]
        rack_word=''.join(rack_word1)
        rack_list.append(rack_word)
else:
    print("Error: You failed to provide valid wildcards. Wildcards can be either * or ?, and a total of two wild cards at most (one of each character).")
    sys.exit()

# funtion that counts the letters in a word and return a dictionary
def count_letters(word):
    count = {}
    for letter in word.lower():
        count[letter] = count.get(letter,0) + 1
    return count

for x in rack_list:
    rack_count = count_letters(x)
    valid_words = []

    for word in data:
        word_count = count_letters(word)
        intersec = set(word.lower()).intersection(set(x.lower()))
        letter_number = [(word_count[letter],rack_count[letter]) for letter in intersec]

        check1 = all(item[0] <= item[1] for item in letter_number)
        check2 = set(word.lower()) <= set(x.lower())
        if check1 and check2:
            valid_words.append(word)

score_list = [(word, score(word)) for word in valid_words]
new_list = sorted(score_list, key=lambda x: x[1], reverse=True)
print(rack.upper(), "-> ", len(new_list), "words")
print(new_list)
