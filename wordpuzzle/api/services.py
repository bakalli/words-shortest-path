# api/services.py
import asyncio
import string
from .word_loader import WordLoader
from collections import deque 

class WordPuzzleSolverService:
    
    def __init__(self): 
        self.word_loader = WordLoader()
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
        self.build_graph(start_word, end_word)
        
        # run shortest path algorithm
        queue = deque()
        visited = set()
        queue.appendleft(start_word)
        previous = {start_word: None}
        while queue: 
            node = queue.pop()
            if node == end_word:
                break 
            visited.add(node)
            neighbors = self.graph[node]
            for neighbor in neighbors: 
                if neighbor not in visited:
                    previous[neighbor] = node
                    queue.appendleft(neighbor)
        # rebuild from previous pointer
        if end_word not in previous:
            return [] # what should I be returning here? No path found, some HTTP code situation? 
        node = end_word
        path = [end_word]
        while node!=start_word: 
            path.append(previous[node])
            node = previous[node]
        return path[::-1]
    
    def build_graph(self, start_word, end_word):
        # update self.graph with the adjacency list (node -> edges) of traversable words from start and end word 
        if len(start_word) != len(end_word):
            return 
        self.graph = {} # clear graph in case of previous, consider turning this into a non instance parameter
        # possible efficiency improvement - only need to use one node, since if they connect then anything reachable from start will be reachable from end
        nodes = [start_word, end_word]
        discovered = set()
        while nodes: 
            node = nodes.pop()
            if node not in self.graph:
                self.graph[node] = set()
            discovered.add(node)
            neighbors = self.get_neighbors(node)
            for neighbor in neighbors:
                self.graph[node].add(neighbor)
                if neighbor not in discovered: 
                    nodes.append(neighbor)    
    
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







    
