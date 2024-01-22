from django.test import TestCase

# Create your tests here.


"""
WordPuzzleSolverService Test Suite: 

    solve_puzzle integration testing: 
        fail cases: words are not of equal length -> throw error , empty string or invalid word provided -> [] no solution 
        coverage: single letter, multi letter, unsolveable

    build_graph unit testing: 
        fail cases: words are not same length, empty string provided, invalid word provided --> []
        invariant: all nodes must be same length as originally provided words
        coverage: single letter, multi letter 

    get_neighbors unit testing: 
        fail cases: empty string provided, invalid word provided --> []
        invariant: all neighbors must be same length as original word
        coverage: 0 < word_length < max_word_length + 1

"""
