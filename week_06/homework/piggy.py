### is_consonant function

def is_consonant(char):

    "takes a character and returns True if it is a consonant"

    if char not in 'aeiou':
        return True
    else:
        return False

### to_piglatin function

def to_piglatin(words):

    """takes a word, moves all starting consonants (all consonants before the first vowel) to the end of the word,
    then adds ay to the end and returns the result.
    Have this function check whether or not the input is multiple words and return the whole sentence in pig latin.
    For this you may assume that a sentence always ends with a period and the input is always one sentence,
    never more than one.

    This function also assumes that the sentence only contains letters and ',', no numbers and other characters. """

    # check whether or not input is a sentence with a period at the end.
    #if yes, return the whole sentence in pig latin


    # Check whether or not a sentence. If yes, get rid of '.' and split the sentence to word list

    # the sentence

    if words[-1] == '.':

        splitword=words[:-1].split()

        # newwordlst is a list that holds the the pig latin words in the sentence
        # check each word in the list for the first vowel and get its index number,
        # then stop the loop after finding the first vowel for each word using break statement.
        # make the new word using the found index number and pig latin rule.
        # append the pig latin word to the newwordlst


        newwordlst=[]

        for word in splitword:
            for char in word:

                # assumes the word in the sentence only contains letters, no numbers or other characters.
                # numbers or other characters will be treated as vowels if existed.

                if not is_consonant(char):
                    j = word.index(char)
                    break

            # This program only checks if ',' in the word. if yes, move ',' to the end of newword
            # the other special characters other than ',' in the middle of the sentence
            # are assumed out of the scope of the function.

            if ',' not in word:
                newword=word[j].upper() + word[j+1:].lower() + word[0:j].lower() + "ay"

            else:
                newword=word[j].upper() + word[j+1:-1].lower() + word[0:j].lower() + "ay,"

            newwordlst.append(newword)

        # turn the newwordlst into a string, add the period at the end, return the string

        return ' '.join(newwordlst) + '.'

    # if not a sentence, check the word for the first vowel, and get the index of the first vowel

    else:
        for char in words:
            if not is_consonant(char):
                j = words.index(char)
                break
        newword=words[j].upper() + words[j+1:].lower() + words[0:j].lower() + "ay"
        return newword

print("to_piglatin('stay') -> ", to_piglatin('stay'))
print("to_piglatin('Jared') -> ", to_piglatin('Jared'))
print("to_piglatin('and') -> ", to_piglatin('and'))
print("to_piglatin('car') -> ", to_piglatin('car'))
print("to_piglatin('You need to stay in the car, not in the builing, not in the cafe.') -> ", to_piglatin('You need to stay in the car, not in the builing, not in the cafe.'))
