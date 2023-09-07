#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Paul Martin Enano
# email: enano1@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for r in range(3):
            for c in range(3):
                self.tiles[r][c] = digitstr[3*r + c]

                if self.tiles[r][c] == '0':
                    self.blank_r = r
                    self.blank_c = c

    

    ### Add your other method definitions below. ###
    def __repr__(self):
        """returns a string representation of a Board object
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for r in range(3):

            for c in range(3):
                if self.tiles[r][c] == '0':
                    s+= '_' + ' '
                else:
                    s += self.tiles[r][c] + ' '

            s += '\n'  # newline at the end of the row

        return s
    
    def move_blank(self, direction):
        """takes as input a string direction that specifies the direction
        in which the blank should move, and that modifies the contents of the called 
        board object. Not all moves are possible on a given board, 
        ex. it can't go down if it is already on the botton row, method returns TRUE or FALSE
        to indicate is the move is possible
        """
        
      
        if self.blank_r == 0 and direction == 'up':
            return False
        #else:
            #return True
            #can I change all of the self.tiles in between these if else statements?
        elif self.blank_r == 2 and direction == 'down':
            return False
        elif self.blank_c == 0 and direction == 'left':
            return False
        elif self.blank_c == 2 and direction == 'right':
            return False
        else:
            
            if direction == 'up' :
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r-1][self.blank_c]
                self.tiles[self.blank_r-1][self.blank_c] = '0'
                self.blank_r = self.blank_r-1
            elif direction == 'down' :
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r+1][self.blank_c]
                self.tiles[self.blank_r+1][self.blank_c] = '0'
                self.blank_r = self.blank_r+1
            elif direction == 'left' :
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][self.blank_c-1]
                self.tiles[self.blank_r][self.blank_c-1] = '0'    
                self.blank_c = self.blank_c-1
            elif direction == 'right' :
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][self.blank_c+1]
                self.tiles[self.blank_r][self.blank_c+1] = '0'
                self.blank_c = self.blank_c+1
            else:
                return False
            return True

    def digit_string(self):
        """creates and returns a string of digits that corresponds to the current contents of the 
        called Board object's tiles atttribute.
        """
        s = ''
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == '_':
                    s+= '0'
                else:
                    s += self.tiles[r][c]
        return s
    
    def copy(self):
        """returns a newly-constructed Board object 
        that is a deep copy of the object
        """
        string = self.digit_string()
        newboard= Board(string)
        
        return newboard
    
    def num_misplaced(self):
        """counts and returns the number of tiles in the called Board object that are not where they
        should be in the goal state. Not including the blank cell in this count
        """
        count = 0
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == '_' or self.tiles[r][c] == '0':
                    count -= 0
                elif self.tiles[r][c] != GOAL_TILES[r][c]:
                    count += 1
    
        return count
    
    def __eq__(self, other):
        """that can be called whhen the == operator is used to compare two Board objects.
        The method returns True if the called object (self) and the argument (other) have
        the same values for the tiles attribute, and False otherwise
        """
        if self.tiles == other.tiles:
            return True
        else:
            return False