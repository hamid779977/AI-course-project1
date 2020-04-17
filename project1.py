# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation
from search import Graph


def bfs(graph, start, goal):
    # Your Code Here
    raise NotImplementedError


# Once you have completed the breadth-first search,
# this part should be very simple to complete.
def dfs(graph, start, goal):
    # Your Code Here
    raise NotImplementedError


# Now we're going to try optimal search.  The previous searches haven't
# used edge distances in the calculation.

# This function takes in a graph and a list of node names, and returns
# the sum of edge lengths along the path -- the total distance in the path.

def path_length(graph, node_names):
    # Your Code Here
    raise NotImplementedError


def uniform_cost_search(graph, start, goal):
    # Your Code Here
    raise NotImplementedError


def a_star(graph, start, goal):
    # Your Code Here
    raise NotImplementedError


# It's useful to determine if a graph has a consistent and admissible
# heuristic.  You've seen graphs with heuristics that are
# admissible, but not consistent.  Have you seen any graphs that are
# consistent, but not admissible?

def is_admissible(graph, goal):
    # Your Code Here
    raise NotImplementedError


def is_consistent(graph, goal):
    # Your Code Here
    raise NotImplementedError
