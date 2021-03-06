import random

letters_guessed = [] 
letters_not_guessed = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()


    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):

    word = []

    for char in secret_word:
        if char in letters_guessed:
            word.append(char)

    return "".join(word) == secret_word

    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed 

def get_guessed_word(secret_word, letters_guessed):
    # secret_word = list(secret_word)

    letter_blanks = []

    for i in range(len(secret_word)):
        letter_blanks.append("_")

    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            letter_blanks[i] = secret_word[i]       



    return "".join(letter_blanks)


    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    

def is_guess_in_word(guess, secret_word):

    return guess in list(secret_word)
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word

  
def print_game():
    print("Guessed word so far: "+ get_guessed_word(secret_word, letters_guessed))
    print("These letters haven't been guessed yet: " + "".join(letters_not_guessed))
    print("_________________________________________")


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    guesses = 7
    print("Welcome to Spaceman!")
    print("The secret word contains: " + str(len(secret_word)) + " letters.")
    print("You have 7 incorrect guesses, please enter one letter per round")
    print("_________________________________________")

    while guesses != 0 and not is_word_guessed(secret_word, letters_guessed):
        guessed_letter = input("Enter a letter: ")


        # Handles invalid guess

        if len(guessed_letter) != 1 or guessed_letter in letters_guessed:
            print("Invalid guess")

        # Handles correct guess 
        elif (is_guess_in_word(guessed_letter, secret_word)):
            letters_guessed.append(guessed_letter)
            letters_not_guessed.pop(letters_not_guessed.index(guessed_letter))
            print(guessed_letter + " was found!")
            print_game()

        # Handles incorrect guess

        else:
            letters_guessed.append(guessed_letter)
            letters_not_guessed.pop(letters_not_guessed.index(guessed_letter))
            guesses -= 1
            print("Sorry your guess was not in the word, try again")
            print("You have " + str(guesses) + " remaining")
            print_game()
    

    # Handle win game logic
    if guesses > 0:
        print("Congratulations, you won")
    else:
        # Lose game logic
        print("You lost, the word was " + secret_word)



    #TODO: show the player information about the game according to the project spec
    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far
    #TODO: check if the game has been won or lost


def test_guessed_word():
    assert get_guessed_word(("mondale"), ['d','e', 'l', 'm']) == "m__d_le"


def test_is_guess_in_word(): #tests to see if user letter guessed is correct
    assert is_guess_in_word(("m"), ('mondale')) is True


def test_word_guessed(): #tests to see if user guesses word correctly
    assert is_word_guessed(("mondale"), ['m', 'o', 'n', 'd', "a", "e"]) is False


if __name__ == "__main__":
    secret_word = load_word()
    spaceman(secret_word)
    # Run the test function
    test_guessed_word()