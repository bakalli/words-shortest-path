from django.test import TestCase
import unittest

"""
WordPuzzleSolverService Test Suite: 

    solve_puzzle integration testing: 
        fail cases: words are not of equal length -> throw error , empty string or invalid word provided -> throw error 
        edge case: startWord and endWord are the same
        coverage: single letter, multi letter, unsolveable, graph has cycles

    build_graph unit testing: 
        fail cases: words are not same length, empty string provided, invalid word provided --> throws upstream in solve_puzzle
        invariant: all nodes must be same length as originally provided words
        coverage: single letter, multi letter 

    get_neighbors unit testing: 
        fail cases: empty string provided, invalid word provided --> throws upstream in solve_puzzle
        invariant: all neighbors must be same length as original word
        coverage: 0 < word_length < max_word_length + 1

"""

class WordPuzzleSolverTests(unittest.TestCase): 
    def test_get_neighbors_small(self):
        ...
    def test_get_neighbors_medium(self):
        ...
    def test_get_neighbors_large(self):
        ...
    def test_build_small_graph(self): 
        ...
    def test_build_medium_graph(self): 
        ...
    def test_build_large_graph(self):
        ...
    def test_simple_shortest_path(self): 
        ...
    def test_medium_shortest_path(self):
        ...
    def test_full_shortest_path(self):
        ...
    def test_shortest_path_with_cycle(self):
        ...
    def test_shortest_path_differing_word_lengths(self):
        ...
    def test_shortest_path_invalid_or_empty_word(self):
        ...
    def test_shortest_path_unsolveable(self): 
        ...
