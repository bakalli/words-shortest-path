# api/services.py
import asyncio
import WordLoader from word_loader

class WordPuzzleSolverService:
    
    def __init__(self): 
        self.word_loader = WorldLoader()
        self.word_loader.load_words()
        self.graph = {}
    
    async def solve_puzzle(start_word, end_word): 
        #asynchronous logic for solving word puzzle
        result = []
        return result
    
    def build_graph(self, start_word, end_word):
        # update self.graph with the adjacency list (node -> edges) of traversable words from start and end word 
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







    
