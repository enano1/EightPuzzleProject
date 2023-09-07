#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    def __init__(self, depth_limit):
        """constructs a new Searcher object
        """
        self.states = []
        self.num_tested = 0
        if depth_limit == None:
            self.depth_limit = -1
        else:
            self.depth_limit = depth_limit

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s

    def add_state(self, new_state):
        """takes a single State object called new_states and adds it to the 
        Searcher's list of untested states.
        """
        self.states += [new_state]
        
    def should_add(self, state):
        """takes a State object called state and returns True
        if the Searcher should add states to its list of 
        untested states, and False otherwise
        """
        if (self.depth_limit != -1 and state.num_moves > self.depth_limit) or state.creates_cycle() == True:
            return False
        else:
            return True
        
    def add_states(self, new_states):
        """takes a list State objects called new_states, and processes the elements
        of new_states one at a time
        """
        for s in new_states:
            if self.should_add(s) == True:
                self.add_state(s)

    def next_state(self):
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s    
                
    def find_solution(self, init_state):
        """preforms a full state-space search that begins at the specified initial sate init_state
        and ends when the goal state is found or when
        the Searcher runs out of untested states.
        """
        self.add_state(init_state)
        
        while self.states != []:
            s =  self.next_state()
            self.num_tested += 1
            if s.is_goal()==True:
                return s
            else:
                self.add_states(s.generate_successors())
        #self.add_states(init_state.generate_successors())
            
        
            #for i in self.states:
                #self.add_states(i.generate_successors())
            
                #s =  self.next_state()
                #if s.is_goal() == True:
                    #return s
                
        return None
            
    
        
        #now the last searcher.should_add(s3) returns True instead of false
### Add your BFSeacher and DFSearcher class definitions below. ###
class BFSearcher(Searcher):
    def next_state(self):
        s = self.states[0] 
        self.states.remove(s) 
        return s

class DFSearcher(Searcher):
    def next_state(self):
    
        s = self.states[-1] 
        self.states.remove(s) 
        return s



def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###
def h1(state):
    """ a heuristic function that returns an estimate of how many
    additional moves are needed to get from state to the goal state
    """
    return state.board.num_misplaced()

def h2(state):
    """ a heuristic function, that distinguishes puzzles
    based on how many moves it can be completed in
    """
    rowcount = 0
    columncount = 0
    columnGOAL = [['0', '3', '6'],['1', '4', '7'],['2', '5', '8']]
    
    for r in range(3):
        for c in range(3):
            if state.board.tiles[r][c] not in GOAL_TILES[r]:
                if state.board.tiles[r][c] == '_' or state.board.tiles[r][c] == '0':
                    rowcount += 0
                else:
                    rowcount += 1
            if state.board.tiles[r][c] not in columnGOAL[c]:
                if state.board.tiles[r][c] == '_' or state.board.tiles[r][c] == '0':
                    columncount += 0
                else:
                    columncount += 1
    return rowcount + columncount
    
#for this, it's [state.priority(state), state] 
#but for the number, we need to use the num.moves

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    def __init__(self, heuristic):
        """constructs a new GreedySearcher object
        """
        super().__init__(-1)
        self.depth_limit = -1
        self.heuristic = heuristic
        
        

    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s

    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)

    def add_state(self, state):
        """ overrides the add_state method inherited from Searcher
        adds a sublist that is a [priority, state] pair
        where priority is the priority of state that is
        determined by calling the priorty method
        """
        self.states += [[self.priority(state), state]]
        
    def next_state(self):
        """overrides the next_state method that is inherited from Searcher
        chooses one of the states with the highest priority
        """ 
        pairs = [[w[0], w[1]] for w in self.states]
        maxpair = max(pairs)
        self.states.remove(maxpair)
        return maxpair[1]
### Add your AStarSeacher class definition below. ###
class AStarSearcher(Searcher):
    def __init__(self, heuristic):
        """a constructor for A* object
        """
        super().__init__(-1)
        self.depth_limit = -1
        self.heuristic = heuristic
       
    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s  
    
    def priority(self, state):
        """ A*'s priority of self method which
        uses the equation  p(x) = -1* h(x) + g(x)
        """
        p = -1 * (self.heuristic(state) + state.num_moves) 
        return p
        
    def add_state(self, state):
        """creates an add_state method for the class
        """
        self.states += [[self.priority(state), state]]
        
    def next_state(self):
        """creates a next_state method for the class
        A*'s priority of self method which
        uses the equation  p(x) = -1* h(x) + g(x)
        """
        pairs = [[w[0], w[1]] for w in self.states]
        maxpair = max(pairs)
        self.states.remove(maxpair)
        return maxpair[1]
    
    
    
    
