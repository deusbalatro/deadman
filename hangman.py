import random
import string
import os, sys
import subprocess

def clearConsole():
    subprocess.call('cls', shell=True)

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    """
    return random.choice(wordlist)


wordlist = load_words()




def is_word_guessed(secret_word, letters_guessed):

    
    counter = 0
    comparison = ["_"]*len(secret_word)
    for letter in secret_word:
        counter += 1
        for let in letters_guessed:
            if letter == let and secret_word.index(letter) == letters_guessed.index(let):
                comparison[counter-1] = let
         
    
    if secret_word == ''.join(comparison):
        return True
    else:
        return False
     
       


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far

    '''
    counter = 0
    new_list = ['_ ']*len(secret_word)
    for letter in secret_word:
            counter += 1
            for let in letters_guessed:
                if letter == let:
                    new_list[counter-1] = letter
                    continue

                
    return ''.join(new_list)         

        



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far

    '''
    all_letters = string.ascii_lowercase
    remained_letters = ''
    for let in all_letters:
        if let not in letters_guessed:
            remained_letters += let
    
    return remained_letters
    

    
    
    
print("Welcome to the Hangman Game!")


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    '''
    print(f"I am thinking of a word that is {len(secret_word)} letters long")
    right = 6
    right_check = right
    warning = 3
    letters_guessed = []
    print(f"You have {warning} warnings left")
    print(f"You have {right} guesses left.")
    print(f"Available letters: {get_available_letters(letters_guessed)}")
    while right > 0:
        
        print("---------------")
        vowels = ['a', 'e', 'i', 'o', 'u']
        new_guess = input("Please guess a letter: ").lower()
        if not new_guess.isalpha():
            warning -= 1
            if warning < 0:
                right -= 1
                print(f"Oops! That is not a valid letter. You do not have any warnings left, thus I am taking a guess from you. {right} guess left.")
                continue
            print(f"Oops! That is not a valid letter. {warning} warnings left")
            continue
        if len(new_guess) > 1 and len(new_guess) < len(secret_word):
            right -= len(new_guess)
            print(f"You punished! {right} guess left")
            continue
        
        if new_guess in letters_guessed:
            warning -= 1
            if warning < 0:
                right -= 1
                print(f"You already did this guess. You do not have any warnings left, thus I am taking a guess from you. {right} guess left.")
                continue
            else:
                print(f"you already did this guess. {warning} warning left.")
                print(f"Available letters: {get_available_letters(letters_guessed)}")
                continue
        else:
            letters_guessed += new_guess

            
            if new_guess in secret_word:
                print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
                if is_word_guessed(secret_word, letters_guessed):
                    break
                print(f"You have {right} guesses left")
                print(f"Available letters: {get_available_letters(letters_guessed)}")
            else:
                if new_guess in vowels:
                    right -= 2
                    if right <= 0:
                        print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
                        break
                    else:
                        print(f"Oops! That letter is not in my word and it was a vowel!: {get_guessed_word(secret_word, letters_guessed)}")
                        print(f"You have {right} guesses left")
                        print(f"Available letters: {get_available_letters(letters_guessed)}")
                else:
                    
                    right -= 1
                    if right <= 0:
                        print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
                        break
                    else:

                        print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
                        print(f"You have {right} guesses left")
                        print(f"Available letters: {get_available_letters(letters_guessed)}")
            
    unique_letters = []
    for char in secret_word:
        if char not in unique_letters:
            unique_letters += char
    
    score = right*len(unique_letters)
    if right > 0:
        print("You won!")
        print(f"Your total score for this game is: {score}")
    else:
        print("Sorry, you ran out of guesses. The word was else.")

    return get_guessed_word(secret_word, letters_guessed)
    
    






# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    
    '''
    my_word = list(my_word)
    for char in my_word:
        if char == ' ':
            my_word.remove(char)

    checked_letters = []
    other_word = list(other_word)
    counter = 0


    if len(my_word) != len(other_word):
        return False
    else:
        for char in my_word:
           
            
            if char != '_' and char == other_word[counter]:
                
                if my_word.count(char) != other_word.count(char):
                    
                    return False
                        
                
                counter += 1
                
            else:
                if char == '_':
                    counter += 1

                    
                else:

                    return False
        
       
    return True





def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word

    '''
    matched_words = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            ''.join(word)
            matched_words.append(word)
    print(', '.join(matched_words))
    





def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    '''
   
    print(f"I am thinking of a word that is {len(secret_word)} letters long")
    right = 6
    right_check = right
    warning = 3
    letters_guessed = []
    print(f"You have {warning} warnings left")
    print(f"You have {right} guesses left.")
    print(f"Available letters: {get_available_letters(letters_guessed)}")
    while right > 0:
        
        print("---------------")
        vowels = ['a', 'e', 'i', 'o', 'u']
        new_guess = input("Please guess a letter: ").lower()
        if not new_guess.isalpha():
            
            if new_guess == '*':
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
                continue
            else:

                warning -= 1
                if warning < 0:
                    right -= 1
                    print(f"Oops! That is not a valid letter. You do not have any warnings left, thus I am taking a guess from you. {right} guess left.")
                    continue
                print(f"Oops! That is not a valid letter. {warning} warnings left")
                continue
        if len(new_guess) > 1: 
            if len(new_guess) < len(secret_word):
                right -= len(new_guess)
                print(f"You punished! {right} guess left")
                continue
            elif len(new_guess) == len(secret_word):
                if is_word_guessed(secret_word, new_guess):
                    break
                else:
                    print(f"Oops! That word is not my word: {get_guessed_word(secret_word, letters_guessed)}")
                    right -= 1
                    print(f"You have {right} guesses left")
                    print(f"Available letters: {get_available_letters(letters_guessed)}") 
                    continue
        
        elif new_guess in letters_guessed:
            warning -= 1
            if warning < 0:
                right -= 1
                print(f"You already did this guess. You do not have any warnings left, thus I am taking a guess from you. {right} guess left.")
                continue
            else:
                print(f"you already did this guess. {warning} warning left.")
                print(f"Available letters: {get_available_letters(letters_guessed)}")
                continue
        else:
            letters_guessed += new_guess

            if new_guess in secret_word:
                print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
                
                if is_word_guessed(secret_word, get_guessed_word(secret_word,letters_guessed)):
                    break
                print(f"You have {right} guesses left")
                print(f"Available letters: {get_available_letters(letters_guessed)}")
            else:
                if new_guess in vowels:
                    right -= 2
                    if right <= 0:
                        print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
                        break
                    else:
                        print(f"Oops! That letter is not in my word and it was a vowel!: {get_guessed_word(secret_word, letters_guessed)}")
                        print(f"You have {right} guesses left")
                        print(f"Available letters: {get_available_letters(letters_guessed)}")
                else:
                    
                    right -= 1
                    if right <= 0:
                        print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
                        break
                    else:

                        print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
                        print(f"You have {right} guesses left")
                        print(f"Available letters: {get_available_letters(letters_guessed)}")
                
    unique_letters = []
    for char in secret_word:
        if char not in unique_letters:
            unique_letters += char
    
    score = right*len(unique_letters)
    if right > 0:
        print("You won!")
        print(f"Your total score for this game is: {score}")
    else:
        print("Sorry, you ran out of guesses. The word was else.")

    return get_guessed_word(secret_word, letters_guessed)





x = input("wanna play?\n")

if x == 'q' or x == 'no' or x == 'quit' or x == 'exit' or x == 'n':
    sys.exit()

else:
    if __name__ == "__main__":

        secret_word = choose_word(wordlist)
        
        hangman_with_hints(secret_word)
        
        x = input("wanna play?")
        os.system('cls')
        os.system('clear')