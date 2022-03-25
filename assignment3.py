#----------------------------------------------------
# Assignment 3: Skittles 175
# 
# Author: CMPUT 175 team
#----------------------------------------------------

from skittles import SkittleGame

def displayWelcome(welcome):
    '''Displays a simple welcome banner. Input: welcome string. Nothing is returned.'''    
    print("="*len(welcome))
    print(welcome)
    print("="*len(welcome))
    

def initializeFromFile(filename):
    '''
    Reads in the size of the Skittle's gameboard from a file, as well
    as the colours of all of the playing skittles.
    
    Inputs:
       filename (str) - the name of the file to read the data from
    Returns:
       rows (int) - the number of rows of the gameboard (i.e. number of stacks)
       columns (int) - the number of columns of the gameboard (i.e. capacity of stacks)
       skittleColours (list of str) - colours of playing skittles, in the order they are to be played
    '''
    try:
        fin = open(filename)
    except OSError:
        raise
    else:
        # gameboard dimensions are in first line
        dimensions = fin.readline() 
        rows, columns = dimensions.strip().split()
        
        # colours of playing skittles are all in second line
        colours = fin.readline()
        skittleColours = colours.strip().split(',')
        
        fin.close() # don't forget to close the file!
    return (int(rows), int(columns), skittleColours)    


def validateIntEntry(prompt, low, high):
    '''
    Prompts the user to enter an integer with a custom prompt.
    Verifies that the entry is a number between low and high; 
    reprompts if it is not.  Note that this does not reprompt
    if a non-integer is entered (that will raise an exception).
    
    Inputs:
       prompt (str)
       low (int)
       high (int)
    Returns:
       valid integer
    '''
    entry = int(input(prompt))
    while entry < low or entry > high:
        print("Invalid entry.", end = '')  # tell the user that something is wrong with entry
        entry = int(input(prompt))         # reprompt
    return entry
    
    
def main():
    '''
    Basic implementation of the Skittles game for assignment #3. No inputs. Nothing is returned.
    '''
    displayWelcome('Welcome to SKITTLES 175')
    filename = input('\nPlease enter a filename to initialize game: ')
    try:
        # initialize game
        rows, columns, colourList = initializeFromFile(filename)
        game = SkittleGame(rows, columns)
        game.populateDeck(colourList)
                
        # display starting gameboard
        print('')
        game.displayGame()
        
        # play game
        while not game.isWon() and not game.isLost():
            skittle = game.dealSkittle() 
            stackPrompt = '\nWhich stack would you like to play {} on ({}-{})? '.format(skittle, 0, rows-1)
            stackNum = validateIntEntry(stackPrompt, 0, rows-1)
            while not game.playSkittle(stackNum, skittle):
                print('Could not play on stack {} because it is full'.format(stackNum))
                stackNum = validateIntEntry(stackPrompt, 0, rows-1)
            game.displayGame()
        
        # why did the game end?
        if game.isWon():
            # display winning message if there are no more playing skittles, even if board is also full
            print('\nWINNER! All skittles have been successfully played.') 
        else:
            # otherwise, display losing message
            print('\nGAME OVER. Better luck next time.')
                    
    
    # NOTE: you may wish to comment out try and excepts while debugging
    except OSError:
        print('Cannot initialize game based on {}.'.format(filename), end = ' ')
    except AssertionError as error:
        print('Invalid input:', error.args)
    except Exception as unknownError:
        print(unknownError.args)
    finally:
        print('Goodbye.')

        
if __name__=='__main__':
    main()