
## How to run

```shell
cd wordpuzzle
python manage.py runserver
```

## Example GET request sent over the API 

Once our django server is running locally, we can send get requests 
by passing our start and end words as query parameters in our URL. 

```
startWord: oyster
endWord: mussel

http://127.0.0.1:8000/api/wordpuzzle?startWord=oyster&endWord=mussel
```

## Testing and Implementation Details

To run the automated tests for the word-puzzle, you can run the below line of code in command line:

```
python3 manage.py test
```

If all tests pass as expected, this will yield the following: 

```
----------------------------------------------------------------------
Ran 12 tests in 2.953s

OK
```
### What are we testing? 
These tests have coverage over various parts of the puzzle solver, and are named appropriately for whichever
functionality they are testing. There is a combination of unit tests and integration tests, testing 
the following: 
* Puzzle solver helper methods used to build the graph representation of the puzzle. These methods, 
namely get_neighbors and build_graph, transform the provided dictionary of valid words into an easily 
accessible adjacency list of nodes and edges. 
* The shortest path algorithm, which uses traditional breadth first search traversal. The algorithm 
is simplified by the unweighted nature of our graph, and you can learn more about it by referencing 
Djikstra's Algorithm in an unweighted graph. 
* API access, which uses GET requests to feed pairs of start and end words to our puzzle solver. 

For a more thorough description of test coverage, please refer to the test suite docstring in tests.py 

### Request Lifecycle & Algorithmic Details

When a user queries our API with a GET request as described in previous sections, the request is routed 
through our `WordPuzzleApi` class, which can be found in views.py. This is an instance class, and
creates an accompanying instance of the `WordPuzzleSolverService` class (defined in services.py) upon creation. 
Neither of these classes need be instance classes to solve the puzzle, and can be implemented as static classes. 
However, this implementation allows us to minimize how often we need to load the dictionary, which is a high 
time complexity operation, namely O(V) where V is the size of our dictionary for loading words. This is also
a high space complexity operation, O(V) as well when we store the dictionary in memory. 

The `WordPuzzleSolverService` builds the necessary graph, and runs a shortest path algorithm using BFS graph traversal, returning the shortest path if one exists. We build the graph in O(V'*E) time, where V' in the worst case is the same as the V in the previous paragraph, i.e. every word in the dictionary. However, in a sparsely connected graph, V' will be significantly smaller than V. This is the case because V' is defined only by the nodes reachable from our start node, and since most words in the dictionary are
unreachable (as defined in the puzzle description) from most other words in the dictionary, we can assume V' << V. E is the average
amount of words reachable from a word in the dictionary. 

Once the graph is built, the shortest path algorithm runs in O(V'+(V'*E)) time, since in the worst case, we traverse through each edge and node of the graph. 

Once the puzzle is solved, the solution is returned to the `WordPuzzleApi` and wrapped in JSON, before being returned as a response. In summary, the order of operations can be loosely described as: 

`GET request -> Api Instance created -> Service instance created -> Words loaded -> service builds graph -> service finds shortest path -> shortest path is returned to Api class -> result is wrapped in JSON and returned as response` 


