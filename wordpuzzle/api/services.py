# api/services.py
import asyncio
import WordLoader from word_loader
from collections import deque 

class WordPuzzleSolverService:
    
    def __init__(self): 
        self.word_loader = WorldLoader()
        self.word_loader.load_words()
        self.graph = {}
    
    async def solve_puzzle(start_word, end_word): 
        if len(start_word) != len(end_word):
            raise ValueError("provided start and end word are of different lengths, impossible puzzle")
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
        # rebuild from neighbor list
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
                 if neighbor not in discovered: nodes.append(neighbor)    
    
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







    
