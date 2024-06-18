#Jesse Theophilous

VOWELS = 'aeiouAEIOU'

def main():
    #Asking user for a sentence
    user_input = input('Enter a sentence: ')
    ch = count_vowel(user_input)
    print('There are', ch, 'vowels in', user_input)

#defining another function
def count_vowel(string):
    if not string:
        return 0
    return(1 if string[0] in VOWELS else 0) + count_vowel (string[1: ])


#calling main function
main()
