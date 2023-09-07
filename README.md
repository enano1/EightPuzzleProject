# Eight Puzzle Solver

## Introduction

This is a Python project that provides a solution to the Eight Puzzle problem using various state-space search algorithms. The Eight Puzzle is a classic puzzle that consists of a 3x3 grid with eight numbered tiles and one blank space. The goal is to arrange the tiles in the correct order by sliding them into the blank space.

The project includes the following components:

- `board.py`: Contains the `Board` class, which represents the Eight Puzzle board and its operations.
- `state.py`: Defines the `State` class, representing states in the state-space search tree.
- `searcher.py`: Includes different searcher classes for various state-space search algorithms.
- `eight_puzzle.py`: A driver program to solve Eight Puzzles using different algorithms.
- `timer.py`: A timer utility for measuring the execution time of the algorithms.

## Usage

To use this project, you can follow these steps:

1. Clone the repository to your local machine:
2. Navigate to the project directory:
3. 3. Run the `eight_puzzle.py` script with the desired inputs to solve Eight Puzzles. You can specify the algorithm and input puzzle configuration.
   
The script will display the solution, the number of moves, and other relevant information.

## Algorithms

The project supports various state-space search algorithms, including:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Greedy Search
- A* Search

You can choose the algorithm you want to use when running the `eight_puzzle.py` script.

## Results

The project includes test results for different algorithms with puzzles of various complexities. You can find the results in the `results.txt` file in the project directory.

## Conclusion

The Eight Puzzle Solver project provides a flexible and extensible framework for solving Eight Puzzles using different state-space search algorithms. It's a valuable tool for exploring and comparing the performance of these algorithms in solving puzzles of varying difficulties.                   
