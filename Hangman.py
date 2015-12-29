#Hangman game

#Function to check if the secret word is guessed
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    result = True
    secretWordlist = list(secretWord)
    #print "slist", secretWordlist
    
    for i in secretWordlist:
        #print "value of i:", i
        if i in lettersGuessed:
            result = result and True
        else:
            result = result and False
            
    #print result
    return result      


#Function to print users word
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    guessedlist=[]
    
    # Converting secret word to list
    secretWordlist = list(secretWord)
    l=len(secretWordlist)
    
    # creating a list of same length as secret world but with '- ' s 
    for index in range(l):
        guessedlist.append('_ ')
    
	# Checking if letter guessed matches secret word    
    for i in secretWordlist:
        if i in lettersGuessed:
            # updating guessed list, for correct guesses
            for index in range(l):
                if secretWordlist[index]==i:
                    guessedlist[index]=i

    # Converting guessed list to string for function return                
    guessedWord=''
    for index in range(l):
        guessedWord=guessedWord+guessedlist[index]
    
    return guessedWord


def getAvailableLetters(lettersGuessed):
    lettersavailable=' '
    a=map(chr, range(97, 123))
    alphabetlist=a
    #print a

    l=len(a)
    #print l
        
    for index in range(l):
        #print index, a[index]
        if a[index] in lettersGuessed:
            alphabetlist[index]=' '
    
    #print alphabetlist
            
    for i in alphabetlist:
        if i != ' ':
            lettersavailable=lettersavailable+i
       
    return lettersavailable
    #print lettersavailable

# Hangman game
def hangman(secretWord):
    '''
   secretWord: string, the secret word to guess.
 
   Starts up an interactive game of Hangman.
 
   * At the start of the game, let the user know how many
     letters the secretWord contains.
 
   * Ask the user to supply one guess (i.e. letter) per round.
 
   * The user should receive feedback immediately after each guess
     about whether their guess appears in the computer's word.
 
   * After each round, you should also display to the user the
     partially guessed word so far, as well as letters that the
     user has not yet guessed.
 
   Follows the other limitations detailed in the problem write-up.
   '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' +
          str(len(secretWord)) + ' letters long.')
    print('-------------')
   
    num_guesses = 8
    mistakesMade = 0
    lettersGuessed = []
    while True:
        print('You have ' + str(num_guesses - mistakesMade) +
              ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        guess = raw_input('Please guess a letter: ')
        guess = guess.lower()
        if guess in lettersGuessed:
            str_output = 'Oops! You\'ve already guessed that letter: '
        elif guess in secretWord:
            lettersGuessed.append(guess)
            str_output = 'Good guess: '
        else:
            lettersGuessed.append(guess)
            mistakesMade += 1
            str_output = 'Oops! That letter is not in my word: '
        print(str_output + getGuessedWord(secretWord, lettersGuessed))
        print('-------------')
        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            return
        if mistakesMade == num_guesses:
            print('Sorry, you ran out of guesses. The word was ' +
                  secretWord + '.')
            return


