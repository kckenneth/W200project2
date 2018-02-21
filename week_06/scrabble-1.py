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
#5.
#6.

import sys
from collections import Counter
from score_word import score

#  the official SOWPODS word list constructed as a list named data
with open("sowpods.txt","r") as infile:
    raw_input = infile.readlines()
    data = [datum.strip('\n') for datum in raw_input]
    data = [word for word in data if len(word)<=7]

# check the argument input. if no argument, print error message and exit.
if len(sys.argv) == 2:
    rack=sys.argv[1].lower()
else:
    sys.exit("Error: You need to enter some letters without spaces")

# construct the rack word list using argument and wildcards if any
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
            rack_word2.sort()
            rack_word=''.join(rack_word2)
            rack_list.append(rack_word)
elif number1==1 and number1+number2 < 2:
    for v in 'abcdefghijklmnopqrstuvwxyz':
        rack_word1 = [w.replace('*', v) for w in rack_split]
        rack_word1.sort()
        rack_word=''.join(rack_word1)
        rack_list.append(rack_word)
elif number2==1 and number1+number2 < 2:
    for v in 'abcdefghijklmnopqrstuvwxyz':
        rack_word1 = [w.replace('?', v) for w in rack_split]
        rack_word1.sort()
        rack_word=''.join(rack_word1)
        rack_list.append(rack_word)
else:
    print("Error: You failed to provide valid wildcards. Wildcards can be either * or ?, and a total of two wild cards at most (one of each character).")


#for each word in rack_list, check the valid words by comparing with data list of words
valid_words = []
for x in rack_list:
    rack_count = Counter(x).most_common()
    rack_count.sort()

    for word in data:
        if word in valid_words:
            continue

        elif set(word.lower()) <= set(x.lower()):
            word_count = Counter(word).most_common()
            word_count.sort()
            intersec = set(word.lower()).intersection(set(x.lower()))

            if all(word_count[i][1] <= rack_count[i][1] for i in range(len(intersec))):
                valid_words.append(word)

score_list = [(word, score(word)) for word in valid_words]
new_list = sorted(score_list, key=lambda x: x[1], reverse=True)
print(rack.upper(), "-> ", len(new_list), "words,", "Max Score: ", new_list[0][1])
print(new_list)
