#----------------------------------------------------
# Assignment 3: Skittles 175
# 
# Author: Amrit Aujla
# Collaborators/References: lecture slides and previous labs from CMPUT 175. TA Jack Bazin helped with playSkittle for SkittleGame class
#----------------------------------------------------

class Skittle:
    # Class for skittle in skittles game
    
    RAINBOW = 'ROYGBP' # colours of the rainbow in increasing order
    COMPLEMENTARY_COLOURS = {'R':'GREEN', 'O':'BLUE', 'Y':'PURPLE', 'G':'RED', 'B':'ORANGE', 'P':'YELLOW'}
    
    def __init__(self, colour):
        '''
        Initializes a doubly linked list node that stores information about a skittle. 

        Input:
          - colour (string): valid strings are 'red', 'orange', 'yellow', 'green', 'blue',
                            'purple' with any capitalization
        Returns: None
        '''       
        # check input
        assert colour.upper() in self.COMPLEMENTARY_COLOURS.values(), "Colour must be a string of either red, orange, yellow, green, blue, or purple"
        
        self.__colour = colour[0].upper()  # the colour attribute should not store the whole word
        self.__next = None     # each Skittle always starts as standalone Node
        self.__previous = None # each Skittle always starts as standalone Node


    # DO NOT CHANGE getColour method
    def getColour(self):
        '''Returns the colour of the skittle. No input.'''
        return self.__colour

    
    # DO NOT CHANGE getNext method    
    def getNext(self):
        '''Returns the reference to whatever is next. No input.'''
        return self.__next

    
    # DO NOT CHANGE getPrevious method
    def getPrevious(self):
        '''Returns the reference to whatever is previous. No input.'''
        return self.__previous

    
    def setNext(self, newNext):
        '''
        Updates the next reference.
        Input: newNext - the object that will come next
        Returns: None
        '''         
        # check input
        assert isinstance(newNext, Skittle) or newNext is None, 'newNext must be Skittle or None'
        
        self.__next = newNext

        
    def setPrevious(self, newPrevious):
        '''
        Updates the previous reference.
        Input: newPrevious - the object that will come previous
        Returns: None
        '''       
        # check input
        assert isinstance(newPrevious, Skittle) or newPrevious is None, 'newPrevious must be Skittle or None'
        self.__previous = newPrevious  

        
    def setComplement(self):
        '''Sets the colour attribute to be the complement colour. No inputs. Returns None.'''
        # set colour
        self.__colour = self.COMPLEMENTARY_COLOURS.get(self.__colour)[0]
 
    
    def __lt__(self, anotherSkittle):
        '''
        Checks to see if the Skittle instance is less than anotherSkittle based on their colours
        
        Inputs:
            anotherSkittle: the second Skittle to compare to
            
        Returns: True if the Skittle instance is less than anotherSkittle; False otherwise.
        '''
        # check input
        assert isinstance(anotherSkittle, Skittle), 'Another skittle must be of type Skittle'
        
        # check if Skittle instance is less than anotherSkittle and return bool
        return self.RAINBOW.index(self.__colour) < self.RAINBOW.index(anotherSkittle.getColour())
            
    
    def __gt__(self, anotherSkittle):
        '''
        Checks to see if the Skittle instance is greater than anotherSkittle based on their colours
        
        Inputs:
            anotherSkittle: the second Skittle to compare to
            
        Returns: True if the Skittle instance is greater than anotherSkittle; False otherwise.
        '''
        # check input
        assert isinstance(anotherSkittle, Skittle), 'Another skittle must be of type Skittle'
        
        # check if Skittle instance is greater than anotherSkittle and return bool
        return self.RAINBOW.index(self.__colour) > self.RAINBOW.index(anotherSkittle.getColour())
        
    
    # DO NOT CHANGE __str__ method
    def __str__(self):
        '''Returns the informal string representation of the Skittle. No input.'''   
        return '( ' + self.__colour + ' )'



class SkittleList:
    # Class for list of skittles in skittles game
    
    # DO NOT CHANGE __init__ method
    def __init__(self):
        '''
        Initializes the SkittleList, which is very similar to a Doubly Linked List.
        A SkittleList can only have Skittle and None objects in its sequence.
        Input: N/A
        Returns: None
        '''        
        self.__head = None
        self.__tail = None
        self.__size = 0

        
    # DO NOT CHANGE getSize method
    def getSize(self):
        '''Returns number of Skittles in the sequence. No input.'''
        return self.__size


    # DO NOT CHANGE add method    
    def add(self, skittle):
        '''
        Adds a Skittle to the beginning (head) of the SkittleList and updates the size.
        Notice the similarity between this and the Doubly Linked List add method.
        Input: skittle (must be a Skittle)
        Returns: None
        '''        
        assert isinstance(skittle, Skittle), 'Can only add Skittles to this list'
        
        # ensure node is on its own
        skittle.setPrevious(None) 
        skittle.setNext(None)
        
        # add standalone node to beginning of list
        if self.__head == None:
            self.__tail = skittle
        else:
            self.__head.setPrevious(skittle)
            skittle.setNext(self.__head)
        self.__head = skittle
        self.__size +=1


    # DO NOT CHANGE append method    
    def append(self, skittle):
        '''
        Appends a Skittle to the end (tail) of the SkittleList and updates the size.
        Notice the similarity between this and the Doubly Linked List append method.
        Input: skittle (must be a Skittle)
        Returns: None
        '''         
        assert isinstance(skittle, Skittle), 'Can only append Skittles to this list'
        
        # ensure node is on its own
        skittle.setPrevious(None) 
        skittle.setNext(None)        
        
        # append standalone node to end of list
        if self.__head == None:
            self.__head = skittle
        else:
            self.__tail.setNext(skittle)
            skittle.setPrevious(self.__tail)
        self.__tail = skittle
        self.__size += 1    


    def pop0(self):
        '''Removes and returns the first Skittle in the SkittleList. No input.'''
        # check if SkittleList is empty
        if self.__size == 0:
            raise Exception("Cannot pop from an empty list")
        
        # assign new head and return previous head
        head = self.__head
        self.__head = self.__head.getNext()
        if self.__head != None:
            self.__head.setPrevious(None)
        head.setNext(None)
        
        # update size
        self.__size -=1
        
        return head

        
    def pop(self):
        '''Removes and returns the last Skittle in the SkittleList. No input.'''
        # check if SkittleList is empty
        if self.__size == 0:
            raise Exception("Cannot pop from an empty list")        
        
        # assign new tail and return previous tail
        tail = self.__tail
        self.__tail = self.__tail.getPrevious()
        tail.setPrevious(None)
        if self.__tail != None:
            self.__tail.setNext(None)
        
        # update size 
        self.__size -=1
        
        return tail


    def sortedInsert(self, skittle):
        '''
        Inserts the skittle into the list in increasing order, according to skittle’s colour.
        
        Input:
            skittle: the Skittle to insert 
            
        Returns: None
        '''
        # check input
        assert isinstance(skittle, Skittle), "skittle must be type Skittle"
        
        # find where to insert
        current = self.__head
        previous = None
        while current != None and current < skittle:
            previous = current
            current = current.getNext()
        
        # add skittle to beginning
        if previous == None:
            self.add(skittle)
        
        # append skittle to end
        elif current == None:
            self.append(skittle)
        
        # insert skittle in middle and update size
        else:
            skittle.setPrevious(current.getPrevious())
            skittle.setNext(current)
            current.getPrevious().setNext(skittle)
            current.setPrevious(skittle)
            self.__size +=1
        

    def printReverse(self):
        ''' Displays the skittles in the list on the screen in the reverse order that they appear in the list. No input. Returns None.'''
        
        # keep adding to reverse until nothing left to add
        reverse = ''
        current = self.__tail
        while current != None:
            reverse += str(current)
            current = current.getPrevious()
        
        # print reverse
        print(reverse)


    # DO NOT CHANGE __str__ method
    def __str__(self):
        s = ''
        current = self.__head
        while current != None:
            s += str(current)
            current = current.getNext()
        return s
        

        
class SkittleStack:
    # Class for stack of skittles in skittles game
    
    # DO NOT CHANGE __init__ method
    def __init__(self, capacity):
        '''
        Initializes the SkittleStack, which is essentially a singly linked Stack with a maximum capacity.
        Input: capacity (int) - maximum number of Skittles that can be in Stack at one time
        Returns: None
        '''         
        assert isinstance(capacity, int) and capacity > 0, 'Skittle Stack must have a capacity bigger than 0'
        self.__top = None
        self.__size = 0
        self.__capacity = capacity

        
    def push(self, skittle):
        '''
        Adds the skittle to the top of the Stack, if there is room.
        
        Input:
            skittle: the Skittle to push
            
        Returns: None
        '''
        # check input
        assert isinstance(skittle, Skittle), 'skittle must be Skittle instance'
        
        # check if SkittleStack is full
        if self.__size == self.__capacity:
            raise Exception("Stack is full: cannot push %s onto the stack" % str(skittle))
        
        # push skittle by setting link and update size
        skittle.setPrevious(self.__top)
        self.__top = skittle
        self.__size +=1


    def pop(self):
        '''Removes and returns the top Skittle in the SkittleStack. No input.'''
        # check if SkittleStack is empty
        if self.__size == 0:
            raise Exception( "Cannot pop from an empty stack")
        
        # remove top skittle and update size      
        top = self.__top
        self.__top = self.__top.getPrevious()
        top.setPrevious(None)
        self.__size -=1
        
        return top


    # DO NOT CHANGE getSize method
    def getSize(self):
        '''Returns the number of Skittles currently on the SkittleStack. No inputs.'''
        return self.__size


    # DO NOT CHANGE getCapacity method
    def getCapacity(self):
        '''Returns the maximum number of Skittles that can be on the SkittleStack at once. No inputs.'''
        return self.__capacity    


    # DO NOT CHANGE isEmpty method    
    def isEmpty(self):
        '''Returns True if there are no Skittles on the SkittleStack; False otherwise. No inputs.'''
        return self.__size == 0


    # DO NOT CHANGE isFull method
    def isFull(self):
        '''Returns True if there are the maximum number of Skittles on the SkittleStack; False otherwise. 
           No inputs.'''
        return self.__size == self.__capacity


    def __str__(self):
        '''
        Returns the string representation of the SkittleStack instance. No inputs.
        '''
        
        # add skittles to a string of skittles
        skittles = ''
        current = self.__top
        skittle_length = 5
        field_width = self.__capacity * skittle_length
        while current != None:
            skittles = str(current) + skittles
            current = current.getPrevious()
        
        # add skittles to string and return
        string = "|{0:{1}}|".format(skittles, field_width)
        
        return string
        


class SkittleGame:
    # Class for the skittle game
    
    # DO NOT CHANGE __init__ method
    def __init__(self, rows, columns):
        '''
        Initializes the SkittleGame, which consists of a queue of Skittles that are waiting
        to be played, a gameboard of SkittleStacks to play the Skittles on, a list of Skittles
        that have already been matched (1 skittle for every match-3), and an integer keeping
        track of the highest number of match-3s in a single chain.
        Input: 
           rows (int) - the number of SkittleStacks that will make up the gameboard
           columns (int) - the maximum number of Skittles that can be played in each SkittleStack
        Returns: None
        '''        
        assert isinstance(rows, int) and rows > 0, 'Invalid number of stacks in the game.'
        assert isinstance(columns, int) and columns > 0, 'Invalid height of stacks in the game.'
        
        self.__queue = SkittleList()
        self.__matches = SkittleList()
        self.__maxChains = 0
        self.__board = []
        for i in range(rows):
            self.__board.append(SkittleStack(columns))        

        
    def populateDeck(self, alist):
        '''
        Creates a Skittle for every colour string in alist, and enqueues those Skittles to the back of the playing queue.
        
        Input:
            alist: list of colour strings to create skittles for
            
        Returns: None
        '''
        # add skittle to queue if colours are valid
        try:
            for colour in alist:
                skittle = Skittle(colour)
                self.__queue.append(skittle)
        except AssertionError:
            raise

            
    def dealSkittle(self):
        '''Dequeues the Skittle from the front of the playing queue. No input. Returns None.'''
        # pop skittle from front if queue not empty and return
        try:
            skittle = self.__queue.pop0()
        except Exception:
            raise
        
        return skittle
    
    
    def playSkittle(self, stackNum, skittle, count=0):
        '''
        Attempts to play the provided skittle onto the row (SkittleStack) specified by stackNum.
        Also checks for a match-3 that results from playing the skittle and any chain reactions.
        
        Input:
            stackNum (int): The row number of the stack to play on.
            skittle: The Skittle to play.
            count (int): The number of match-3s that occur after playing skittle
        
        Returns: True if the skittle was successfully added to the specified SkittleStack; False otherwise.
        '''
        try:
            # Try to push skittle
            self.__board[stackNum].push(skittle)
        
        except:
            # Return False if can't push skittle
            return False
        
        else:
            # Otherwise get top 3 skittles and return True
            current = skittle
            if current != None:
                previous = skittle.getPrevious()
                if previous != None:
                    previous_previous = previous.getPrevious()
                    if previous_previous != None:
                        # Check if match
                        if current.getColour() == previous.getColour() and current.getColour() == previous_previous.getColour():
                            
                            # Display match-3/chain reaction message
                            if count == 0:
                                print("Three %s matched on stack %d!" % (skittle, stackNum))
                            else:
                                print("Chain reaction! Three %s matched on stack %s!" % (skittle, stackNum))
                            
                            # Update SkittleStack and call same function with new skittle
                            for i in range(2):
                                skittle = self.__board[stackNum].pop()
                            self.__matches.sortedInsert(skittle)
                            count += 1
                            skittle = self.__board[stackNum].pop()
                            skittle.setComplement()
                            self.playSkittle(stackNum, skittle, count)
                            
                            # Keep track of max chain
                            if count > self.__maxChains:
                                self.__maxChains = count
            
            return True
        
        
    def displayGame(self):
        '''Prints the gameboard, the list of Skittles collected by forming match-3s in decreasing order,
        and the highest number of matches in a single chain to the screen. No input. Nothing is returned.'''
        # Print the gameboard
        for stackNum in range(len(self.__board)):
            print('%d: %s' % (stackNum, self.__board[stackNum]))
        
        # Print list of Skittles collected by forming match-3s and highest # of matches in chain
        print("Matched skittles:", end=' ')
        self.__matches.printReverse()
        print("Highest number of matches in a single chain: %d" % self.__maxChains)
        
    
    def isLost(self):
        '''Returns True if all SkittleStacks (rows) of the gameboard are full; False otherwise. No input.'''
        all_full = True
        
        # if stack is not full, set all_full to False
        for stack in self.__board:
            if not stack.isFull():
                all_full = False
                
        # return True if gameboard is full
        return all_full
 
        
    def isWon(self):
        '''Returns True if all Skittles from the playing queue have been successfully played; False otherwise. No input'''
        # Return True if skittle queue is empty
        return (self.__queue.getSize() == 0)
    


################################
## Functions to Test classes  ##
################################
def testSkittle():
    skittle1 = Skittle('BLue')
    print('\nSkittle 1 is %s' % skittle1)
    
    # Test getColour
    is_pass = (skittle1.getColour() == 'B')
    assert is_pass == True, "fail the test"    
    
    # Try to create skittle with invalid colour
    print('\nTrying to create skittle with invalid colour...')
    try:
        skittle2 = Skittle('pink')
    except AssertionError as err:
        print(err)
    
    # Test getPrevious and getNext for skittle 1
    print('\nThe next of skittle 1 is',skittle1.getNext())
    print('The previous of skittle 1 is',skittle1.getPrevious())
    
    # Create 2 more skittles
    skittle2 = Skittle('green')
    print('\nSkittle 2 is %s' % skittle2)
    skittle3 = Skittle('yellow')
    print('Skittle 3 is %s' % skittle3)
    
    # Set previous and next for skittle 2
    skittle2.setNext(skittle3)
    skittle2.setPrevious(skittle1)
    
    # Test getPrevious and getNext when it is not None
    is_pass = (skittle2.getPrevious() == skittle1 and skittle2.getNext() == skittle3)
    assert is_pass == True, "fail the test"
    
    # Test setPrevious and setNext when input is invalid
    print('\nTrying to set previous and next with invalid input...')
    try:
        skittle1.setNext('hello')
    except AssertionError as err:
        print(err)
    try:
        skittle1.setPrevious('hello')    
    except AssertionError as err:
        print(err)
    
    # Test setComplement
    skittle1.setComplement()
    is_pass = (skittle1.getColour() == 'O')
    assert is_pass == True, "fail the test"    
    
    # Test __lt__ and __gt__
    is_pass = (skittle1 < skittle2 and skittle1 < skittle3)
    assert is_pass == True, "fail the test"    
    
    is_pass = (skittle3 > skittle1 and skittle2 > skittle3)
    assert is_pass == True, "fail the test"  
    
    # Test __lt__ and __gt__ with invalid input
    print('\nTesting __lt__ and __gt__ with invalid input...')
    try:
        skittle1 > 'hello'
    except AssertionError as err:
        print(err)
    try:
        skittle1 < 'hello'
    except AssertionError as err:
        print(err)    
        
    
def testSkittleList():
    skittle1 = Skittle('blue')  
    alist = SkittleList()
    alist.add(skittle1)
    print('')
    print(alist)
    
    # Create Skittles
    skittle2 = Skittle('green')
    skittle3 = Skittle('yellow')
    skittle4 = Skittle('orange')
    skittle5 = Skittle('yellow')
    
    # Test add
    alist.add(skittle2)
    print('\nAfter adding a green skittle: %s' % alist)
    
    # Test add with invalid input
    print('\nTrying to add something other than skittle...')
    try:
        alist.add('hello')
    except AssertionError as err:
        print(err)
        
    # Test size
    is_pass = (alist.getSize() == 2)
    assert is_pass == True, "fail the test"    
    
    # Test append
    alist.append(skittle3)
    print('\nAfter appending a yellow skittle: %s' % alist)
    
    # Test links (the order is skittle2, skittle1, skittle3)
    is_pass = (skittle2.getPrevious() == None and skittle2.getNext() == skittle1 and skittle1.getPrevious() == skittle2 and skittle1.getNext() == skittle3)
    assert is_pass == True, "fail the test"    
    is_pass = (skittle3.getPrevious() == skittle1 and skittle3.getNext() == None)
    assert is_pass == True, "fail the test"        
    
    # Test append with invalid input
    print('\nTrying to append something other than skittle...')
    try:
        alist.append('hello')
    except AssertionError as err:
        print(err)
        
    # Test size
    is_pass = (alist.getSize() == 3)
    assert is_pass == True, "fail the test"
    
    # Test sorted insert
    alist.sortedInsert(skittle4)
    print('\nAfter sortedInsert for a orange skittle : %s' % alist)
    alist.sortedInsert(skittle5)
    print('After sortedInsert for yellow skittle : %s' % alist)
    
    # Test sorted insert with invalid input
    print('\nTrying to insert something other than skittle...')
    try:
        alist.sortedInsert('hello')
    except AssertionError as err:
        print(err)
        
    # Test size
    is_pass = (alist.getSize() == 5)
    assert is_pass == True, "fail the test"     
    
    # Print reverse
    print('\nThe reverse is', end=' ')
    alist.printReverse()
    
    # Test pop0 and pop
    print('\nThe skittle popped from the beginning is', alist.pop0())
    print("Skittle list: %s" % alist)
    print('The skittle popped from the end is', alist.pop())
    print("Skittle list: %s" % alist)
    
    # Test pop0 and pop from empty list
    for i in range(3):
        alist.pop()
    print('\nTrying to pop from empty SkittleList...')
    try:
        alist.pop()
    except Exception as err:
        print(err)
    try:
        alist.pop0()
    except Exception as err:
        print(err)
        
    # Test size when list is empty
    is_pass = (alist.getSize() == 0)
    assert is_pass == True, "fail the test"      
        
    
def testSkittleStack():
    # Creat stack with capacity 4
    stack = SkittleStack(4)
    
    # Push skittle onto stack
    skittle1 = Skittle('BLue')
    stack.push(skittle1)
    print('\nThe stack:',stack)
    
    # Test getCapacity
    is_pass = (stack.getCapacity() == 4)
    assert is_pass == True, "fail the test"
    
    # Test getSize
    is_pass = (stack.getSize() == 1)
    assert is_pass == True, "fail the test"    
    
    # Test isEmpty
    is_pass = (stack.isEmpty() == False)
    assert is_pass == True, "fail the test"    
    
    # Test isFull
    is_pass = (stack.isFull() == False)
    assert is_pass == True, "fail the test"
    
    # Pop the only skittle
    print("\nThe skittle popped is %s" % stack.pop())
    print("The stack now: %s" % stack)
    
    # Test isEmpty now
    is_pass = (stack.isEmpty() == True)
    assert is_pass == True, "fail the test" 
    
    # Try to pop from empty stack
    print('\nTrying to pop from empty stack...')
    try:
        stack.pop()
    except Exception as err:
        print(err)
    
    # Push skittles until full
    stack.push(skittle1)
    skittle2 = Skittle('green')
    stack.push(skittle2)
    skittle3 = Skittle('yellow')
    stack.push(skittle3)
    skittle4 = Skittle('orange')    
    stack.push(skittle4)
    print("\nAfter pushing a blue skittle, then green, then yellow, then orange: %s" % stack)
    
    # Test getSize
    is_pass = (stack.getSize() == 4)
    assert is_pass == True, "fail the test"   
    
    # Test isFull
    is_pass = (stack.isFull() == True)
    assert is_pass == True, "fail the test" 
    
    # Try to push onto full stack
    skittle100 = Skittle('blue')
    print('\nTrying to push onto full stack...')
    try:
        stack.push()
    except Exception as err:
        print(err)
        
    # Try to push something other than skittle
    print('\nTrying to push something other than skittle...')
    try:
        stack.push('hello')
    except Exception as err:
        print(err)
        
    # Test links
    is_pass = (skittle1.getPrevious() == None and skittle1.getNext() == None and skittle2.getPrevious() == skittle1 and skittle2.getNext() == None)
    assert is_pass == True, "fail the test"    
    is_pass = (skittle3.getPrevious() == skittle2 and skittle3.getNext() == None and skittle4.getPrevious() == skittle3 and skittle4.getNext() == None)
    assert is_pass == True, "fail the test"     
    
    
def testGame():
    game = SkittleGame(3, 7)
    # write tests here
    print("\nEmpty game:")
    game.displayGame()
    
    # Test populate deck
    alist = ['yellow', 'yellow', 'yellow', 'purple', 'yellow', 'yellow', 'yellow', 'red', 'blue', 'orange', 'yellow', 'purple', 'red']
    game.populateDeck(alist)
    
    # Deal first 3 skittles (front of alist) in row 0
    print('\nAfter dealing 3 yellow skittles in row 0')
    for i in range(3):
        game.playSkittle(0, game.dealSkittle())
    game.displayGame()
    
    # Test isLost and isWon
    is_pass = (game.isLost() == False)
    assert is_pass == True, "fail the test"
    
    is_pass = (game.isWon() == False)
    assert is_pass == True, "fail the test"
    
    # Deal more skittles
    for i in range(3):
        game.playSkittle(0, game.dealSkittle())
    print('\nAfter dealing more skittles in row 0:')
    game.displayGame()
    
    # Test chain reaction
    print('\nAfter adding yellow to row 0:')
    game.playSkittle(0, game.dealSkittle())
    game.displayGame()
    
    # Fill up row 0
    for i in range(6):
        game.playSkittle(0, game.dealSkittle())
    print('\nAfter filling up row 0 with colours:')
    game.displayGame()
    
    # Try to deal skittle from empty queue
    print('\nTrying to deal from empty stack...')
    try:
        game.playSkittle(0, game.dealSkittle())
    except Exception as err:
        print(err)
    
    # test isWin when playing queue is empty
    is_pass = (game.isWon() == True)
    assert is_pass == True, "fail the test"
    
    # Fill up whole board
    blist = ['red', 'yellow', 'blue', 'orange', 'purple', 'orange', 'yellow', 'yellow', 'orange']
    for i in range(2):
        game.populateDeck(blist)
    for i in range(1,3):
        for j in range(7):
            game.playSkittle(i, game.dealSkittle())
    print('\nAfter filling up board with colours:')  
    game.displayGame()
    
    # Test isLost when board is full
    is_pass = (game.isLost() == True)
    assert is_pass == True, "fail the test"
    
    # test adding colour to full SkittleStack (row 0)
    is_pass = (game.playSkittle(0, game.dealSkittle()) == False)
    assert is_pass == True, "fail the test"    
    
    # Try to populate deck with invalid colours
    print('\nTrying to populate deck with invalid colours...')
    clist = ['pink']
    try:
        game.populateDeck(clist)
    except AssertionError as err:
        print(err)
        
    # Try to create game with invalid size
    print('\nTrying to create game with invalid size...')
    try:
        game1 = SkittleGame('size', 6)
    except AssertionError as err:
        print(err)
    
    # Try to create game with invalid height
    print('\nTrying to create game with invalid height...')
    try:
        game2 = SkittleGame(2, 'height')
    except AssertionError as err:
        print(err)    
        
        
def test_insertion():
    # Create Skittles
    skittle1 = Skittle('blue')
    skittle2 = Skittle('green')
    skittle3 = Skittle('yellow')
    skittle4 = Skittle('orange')
    skittle5 = Skittle('yellow')
    
    alist = SkittleList()
    
    alist.sortedInsert(skittle1)
    print(alist)
    alist.sortedInsert(skittle2)
    print(alist)
    alist.sortedInsert(skittle3)
    print(alist)
    alist.sortedInsert(skittle4)
    print(alist)
    alist.sortedInsert(skittle5)
    print(alist)    
    
    
if __name__=='__main__':
    # comment/uncomment tests as required.  You may add more tests in any format.
    
    #testSkittle()
    #testSkittleList()
    #testSkittleStack()
    #testGame()
    test_insertion()
    
