#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   
#
# name: paul martin enano
# email: enano1@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

from searcher import *
from timer import *

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()

def process_file(filename, algorithm, param):
    file = open(filename)
    solvecount = 0
    movescount = 0
    statestested = 0
    
    for line in file:
        line = line[:-1]
        fields = line.split('\n')
        for i in range(len(fields)):
            fieldsnum = fields[i]
            searcher = create_searcher(algorithm, param)
            newboard = Board(fieldsnum)
            fieldsstate = State(newboard, None, 'init')
            
            soln = None
            try:
                soln = searcher.find_solution(fieldsstate)
                
                if soln==None:
                    print(fieldsnum+':', 'no solution')
                else:  
                    print(fieldsnum +':', str(soln.num_moves), 'moves,', searcher.num_tested, 'states tested')
                    solvecount += 1
                    movescount +=soln.num_moves
                    statestested += searcher.num_tested
            except KeyboardInterrupt:
                print('search terminated, no solution', end='\n')
            #soln = searcher.find_solution(fieldsstate)
    print()
    print('solved', solvecount, 'puzzles' )
    if solvecount !=0:
        print('averages:', float(movescount/solvecount), 'moves,', float(statestested/solvecount), 'states tested')
            






