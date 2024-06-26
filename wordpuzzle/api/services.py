# api/services.py
import asyncio
import string
from .word_loader import WordLoader
from collections import deque 

class WordPuzzleSolverService:
    
    def __init__(self, test_set = None): 
        self.word_loader = WordLoader()
        if test_set == "small":
            self.word_loader.load_words_small()
        elif test_set == "medium":
            self.word_loader.load_words_medium()
        else:
            self.word_loader.load_words()
        self.graph = {}
    
    """
    @param startWord: word from which we are starting our word search.
    @param endWord: word which we are targetting in our search. 
    @return shortest_path: shortest possible path from startWord to endWord, if one exists. 
    """
    def solve_puzzle(self, start_word, end_word): 
        if len(start_word) != len(end_word):
            raise ValueError("Provided start and end words are of different lengths, unsolveable puzzle.")
        word_set = self.word_loader.get_word_set()
        if start_word not in word_set or end_word not in word_set:
            raise ValueError("You have provided an invalid word(s).")
        
        self.build_graph(start_word)
        if end_word not in self.graph:
            raise ValueError("There is no path from startWord to endWord.")
        
        # run shortest path algorithm
        queue = [start_word]
        visited = set()
        previous = {start_word: None}
        while queue:
            next_queue = []
            for node in queue: 
                if node == end_word:
                    next_queue = []
                    break 
                neighbors = self.graph[node]
                for neighbor in neighbors:
                    if neighbor not in visited:
                        previous[neighbor] = node
                        visited.add(neighbor)
                        next_queue.append(neighbor)
            queue = next_queue
        
        node = end_word
        path = [end_word]
        while node!=start_word: 
            path.append(previous[node])
            node = previous[node]
        return path[::-1]
    
    """
    Update self.graph with the adjacency list (node -> edges) of traversable words from starting word.

    @param startWord: word from which we are starting our word search.
    """
    def build_graph(self, start_word):
        self.graph = {} 
        nodes = deque()
        nodes.appendleft(start_word)
        discovered = set()
        while nodes: 
            node = nodes.pop()
            if node in discovered:
                continue
            discovered.add(node)
            if node not in self.graph:
                self.graph[node] = set()
            neighbors = self.get_neighbors(node)
            for neighbor in neighbors:
                self.graph[node].add(neighbor)
                if neighbor not in discovered: 
                    nodes.appendleft(neighbor)    
        return
    
    """
    Get possible neighbors for the given word using the word_set of valid words.
    A neighbor is defined as a word of equal length, which differs by exactly one letter.

    @param word: word for which we are finding neighbors. 
    """
    def get_neighbors(self, word): 
        alphabet = list(string.ascii_lowercase)
        word_set = self.word_loader.get_word_set()
        neighbors = set()
        for i in range(len(word)):
            char = word[i]
            for letter in alphabet: 
                if char == letter: continue 
                possible_neighbor = word[:i] + letter + word[i+1:]
                if possible_neighbor in word_set:
                    neighbors.add(possible_neighbor)
        return neighbors







    
