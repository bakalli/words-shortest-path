from django.test import TestCase
from services import WordPuzzleSolverService
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
        word_service = WordPuzzleSolverService(test_set="small")
        word_set = word_service.word_loader.get_word_set()
        neighbors = word_service.get_neighbors("aaa")
        self.assertEqual(len(neighbors), 3)
        for neighbor in neighbors:
            self.assertTrue(neighbor in word_set)
    def test_get_neighbors_medium(self):
        word_service = WordPuzzleSolverService(test_set="medium")
        word_set = word_service.word_loader.get_word_set()
        neighbors = word_service.get_neighbors("aaaa")
        self.assertEqual(len(neighbors), 4)
        for neighbor in neighbors:
            self.assertTrue(neighbor in word_set)
    def test_get_neighbors_large(self):
        word_service = WordPuzzleSolverService()
        word_set = word_service.word_loader.get_word_set()
        neighbors = word_service.get_neighbors("oyster")
        for neighbor in neighbors:
            self.assertTrue(neighbor in word_set)
    def test_build_small_graph(self): 
        word_service = WordPuzzleSolverService(test_set="small")
        word_service.build_graph("aaa")
        self.assertEqual(len(word_service.graph), 8)
    def test_build_medium_graph(self): 
        word_service = WordPuzzleSolverService(test_set="medium")
        word_service.build_graph("aaaa")
        self.assertEqual(len(word_service.graph), 12)
    def test_simple_shortest_path(self): 
        word_service = WordPuzzleSolverService(test_set="small")
        shortest_path = word_service.solve_puzzle("aaa","bbb")
        self.assertEqual(len(shortest_path), 4)
    def test_medium_shortest_path(self):
        word_service = WordPuzzleSolverService(test_set="medium")
        shortest_path = word_service.solve_puzzle("aaaa","bbbb")
        self.assertEqual(len(shortest_path), 5)
    def test_full_shortest_path_with_cycle(self):
        word_service = WordPuzzleSolverService()
        shortest_path = word_service.solve_puzzle("oyster","mussel")
        self.assertEqual(len(shortest_path), 6)
    def test_shortest_path_differing_word_lengths(self):
        word_service = WordPuzzleSolverService()
        try: 
            shortest_path = word_service.solve_puzzle("oyster","gigantic")
        except Exception as e:
            self.assertIsInstance(e, ValueError)
    def test_shortest_path_invalid_or_empty_word(self):
        word_service = WordPuzzleSolverService()
        try: 
            shortest_path = word_service.solve_puzzle("","")
        except Exception as e:
            self.assertIsInstance(e, ValueError)
        try: 
            shortest_path = word_service.solve_puzzle("ajfuishgsouigh7sogh","ajfuishgs6uighbsogh")
        except Exception as e:
            self.assertIsInstance(e, ValueError)
    def test_shortest_path_unsolveable(self): 
        word_service = WordPuzzleSolverService()
        try:
            shortest_path = word_service.solve_puzzle("nabobrynabobs", "muzzleloading")
        except Exception as e:
            self.assertIsInstance(e, ValueError)

if __name__ == '__main__':
    unittest.main()