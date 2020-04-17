from Project1.search import *
from Project1.graphs import *
from Project1.tester import make_test, get_tests
from Project1.project1 import bfs, dfs
import random
import time

do_bfs = True
try:
    bfs(NEWGRAPH1, 'S', 'H')
except NotImplementedError:
    do_bfs = False

do_dfs = True
try:
    dfs(NEWGRAPH1, 'S', 'H')
except NotImplementedError:
    do_dfs = False

if do_bfs:

    # TEST 1-optional

    def bfs_1_getargs():
        # (graph, start, goal, extended=None, queue=None)
        return [NEWGRAPH1, 'S', 'H']


    def bfs_1_testanswer(val, original_val=None):
        if val and len(val) > 0 and isinstance(val[0], dict):
            raise Exception(
                "Error: Graph functions are supposed to return a list of node *names*, not node dictionaries!")

        return val and list(val) == list('SCDH')


    make_test(type='FUNCTION',
              getargs=bfs_1_getargs,
              testanswer=bfs_1_testanswer,
              expected_val=list('SCDH'),
              name='bfs'
              )


    # TEST 2-optional

    def bfs_2_getargs():
        return [NEWGRAPH2, 'A', 'G']


    def bfs_2_testanswer(val, original_val=None):
        return val and list(val) == list('ASCDFG')


    make_test(type='FUNCTION',
              getargs=bfs_2_getargs,
              testanswer=bfs_2_testanswer,
              expected_val=list('ASCDFG'),
              name='bfs'
              )


    # TEST 3-optional

    def bfs_3_getargs():
        return [NEWGRAPH3, 'S', 'S']


    def bfs_3_testanswer(val, original_val=None):
        return val and list(val) == list('S')


    make_test(type='FUNCTION',
              getargs=bfs_3_getargs,
              testanswer=bfs_3_testanswer,
              expected_val=list('S'),
              name='bfs'
              )


    # TEST 4-optional

    def bfs_4_getargs():
        return [SAQG, 'S', 'G']


    def bfs_4_testanswer(val, original_val=None):
        return val and list(val) == list("SG")


    make_test(type='FUNCTION',
              getargs=bfs_4_getargs,
              testanswer=bfs_4_testanswer,
              expected_val=list("SG"),
              name='bfs')

if do_dfs:
    # TEST 5-optional

    def dfs_1_getargs():
        return [NEWGRAPH1, 'S', 'H']


    def dfs_1_testanswer(val, original_val=None):
        return (NEWGRAPH1.is_valid_path(val) and
                len(NEWGRAPH1.get_connected_nodes(val[-1])) <= 1)


    make_test(type='FUNCTION',
              getargs=dfs_1_getargs,
              testanswer=dfs_1_testanswer,
              expected_val="A valid path along NEWGRAPH1",
              name='dfs'
              )


    # TEST 6-optional

    def dfs_2_getargs():
        return [NEWGRAPH2, 'A', 'G']


    def dfs_2_testanswer(val, original_val=None):
        return (NEWGRAPH2.is_valid_path(val) and
                len(NEWGRAPH2.get_connected_nodes(val[-1])) <= 1)


    make_test(type='FUNCTION',
              getargs=dfs_2_getargs,
              testanswer=dfs_2_testanswer,
              expected_val="A valid path along NEWGRAPH1",
              name='dfs'
              )


    # TEST 7-optional

    def dfs_3_getargs():
        return [NEWGRAPH3, 'S', 'S']


    def dfs_3_testanswer(val, original_val=None):
        return (NEWGRAPH3.is_valid_path(val) and
                len(NEWGRAPH3.get_connected_nodes(val[-1])) <= 1)


    make_test(type='FUNCTION',
              getargs=dfs_3_getargs,
              testanswer=dfs_3_testanswer,
              expected_val="A valid path along NEWGRAPH1",
              name='dfs'
              )


    # TEST 8-optional

    def dfs_4_getargs():
        return [SAQG, 'S', 'G']


    def dfs_4_testanswer(val, original_val=None):
        return (val and (list(val) == list("SQG") or
                         list(val) == list("SAG") or
                         list(val) == list("SG")))


    make_test(type='FUNCTION',
              getargs=dfs_4_getargs,
              testanswer=dfs_4_testanswer,
              expected_val=str(list("SQG")) + " or " + str(list("SAG")),
              name='dfs')


# TEST 1

def path_length_1_getargs():
    return [NEWGRAPH2, list('S')]


def path_length_1_testanswer(val, original_val=None):
    return val == 0


make_test(type='FUNCTION',
          getargs=path_length_1_getargs,
          testanswer=path_length_1_testanswer,
          expected_val=0,
          name='path_length'
          )


# TEST 2

def path_length_2_getargs():
    return [NEWGRAPH1, list('SASAS')]


def path_length_2_testanswer(val, original_val=None):
    return val == 24


make_test(type='FUNCTION',
          getargs=path_length_2_getargs,
          testanswer=path_length_2_testanswer,
          expected_val=24,
          name='path_length'
          )


# TEST 3

def path_length_3_getargs():
    return [NEWGRAPH2, list('HDCECSBSA')]


def path_length_3_testanswer(val, original_val=None):
    return val == 32


make_test(type='FUNCTION',
          getargs=path_length_3_getargs,
          testanswer=path_length_3_testanswer,
          expected_val=32,
          name='path_length'
          )


# TEST 4

def exp_graph(depth):
    g = Graph(["1"])
    goal = 1
    for d in range(depth):
        nodeids = range(2 ** (d + 1), 2 ** (d + 2))
        goal = random.choice(nodeids)
        for nodeid in nodeids:
            parent = nodeid / 2  # intentional integer division
            g.add_edge(str(int(parent)), str(int(nodeid)), 1)
    best_path = [goal]
    while goal > 0:
        goal = goal / 2  # intentional integer division
        best_path.append(goal)
    goal = best_path[0]

    for nodeid in range(1, 2 ** (depth + 1)):
        distance = 0
        shared_parent = nodeid
        while shared_parent not in best_path:
            distance += 1
            shared_parent = shared_parent / 2  # intentional integer division
        g.set_heuristic(str(nodeid), str(goal), distance + best_path.index(shared_parent))
    return g


# TEST 5

def uniform_cost_search_1_getargs():
    return [NEWGRAPH1, 'S', 'G']


def uniform_cost_search_1_testanswer(val, original_val=None):
    return val == list('SCEG')


make_test(type='FUNCTION',
          getargs=uniform_cost_search_1_getargs,
          testanswer=uniform_cost_search_1_testanswer,
          expected_val=list('SCEG'),
          name='uniform_cost_search'
          )


# TEST 6

def uniform_cost_search_2_getargs():
    return [NEWGRAPH1, 'S', 'D']


def uniform_cost_search_2_testanswer(val, original_val=None):
    return val == list('SCD')


make_test(type='FUNCTION',
          getargs=uniform_cost_search_2_getargs,
          testanswer=uniform_cost_search_2_testanswer,
          expected_val=list('SCD'),
          name='uniform_cost_search'
          )


# TEST 7

def uniform_cost_search_6_getargs():
    return [NEWGRAPH4, "S", "T"]


def uniform_cost_search_6_testanswer(val, original_val=None):
    return (val and list(val) == list("SBFHKT"))


make_test(type='FUNCTION_ENCODED_ARGS',
          getargs=uniform_cost_search_6_getargs,
          testanswer=uniform_cost_search_6_testanswer,
          expected_val="correct path for the quiz search problem",
          name='uniform_cost_search'
          )


# TEST 8

def a_star_1_getargs():
    return [NEWGRAPH3, 'S', 'S']


def a_star_1_testanswer(val, original_val=None):
    return list(val) == list('S')


make_test(type='FUNCTION',
          getargs=a_star_1_getargs,
          testanswer=a_star_1_testanswer,
          expected_val=list('S'),
          name='a_star'
          )


# TEST 9

def a_star_2_getargs():
    return [NEWGRAPH1, 'S', 'G']


def a_star_2_testanswer(val, original_val=None):
    return list(val) == list('SCEG')


make_test(type='FUNCTION',
          getargs=a_star_2_getargs,
          testanswer=a_star_2_testanswer,
          expected_val=list('SCEG'),
          name='a_star'
          )


# TEST 10

def a_star_3_getargs():
    return [NEWGRAPH2, 'S', 'G']


def a_star_3_testanswer(val, original_val=None):
    return list(val) == list('SCDFG')


make_test(type='FUNCTION',
          getargs=a_star_3_getargs,
          testanswer=a_star_3_testanswer,
          expected_val=list('SCDFG'),
          name='a_star'
          )


# TEST 11

def a_star_4_getargs():
    return [NEWGRAPH2, 'E', 'G']


def a_star_4_testanswer(val, original_val=None):
    return list(val) == list('ECDFG')


make_test(type='FUNCTION',
          getargs=a_star_4_getargs,
          testanswer=a_star_4_testanswer,
          expected_val=list('ECDFG'),
          name='a_star'
          )

# TEST 12

a_star_test_5_graph = exp_graph(11)
a_star_test_5_goal = list(a_star_test_5_graph.heuristic.keys())[0]
a_star_timing = {'START': 0}


def a_star_5_getargs():
    a_star_timing["START"] = time.time()
    return [a_star_test_5_graph, "1", a_star_test_5_goal]


def a_star_5_testanswer(val, original_val=None):
    elapsed = time.time() - a_star_timing["START"]
    return elapsed < 1 and val[-1] == a_star_test_5_goal


make_test(type='FUNCTION',
          getargs=a_star_5_getargs,
          testanswer=a_star_5_testanswer,
          expected_val=("a_star to take less than one second and get to %s"
                        % a_star_test_5_goal),
          name='a_star'
          )


# TEST 13

def a_star_test_6_getargs():
    return [NEWGRAPH4, "S", "T"]


def a_star_test_6_testanswer(val, original_val=None):
    return list(val) == list("SBCJLT")


make_test(type='FUNCTION_ENCODED_ARGS',
          getargs=a_star_test_6_getargs,
          testanswer=a_star_test_6_testanswer,
          expected_val="correct path for the quiz search problem",
          name='a_star'
          )


# TEST 14

def a_star_7_getargs():
    return [AGRAPH, "S", "G"]


def a_star_7_testanswer(val, original_val=None):
    return val and list(val) == list('SACG')


make_test(type='FUNCTION',
          getargs=a_star_7_getargs,
          testanswer=a_star_7_testanswer,
          expected_val=list('SACG'),
          name='a_star'
          )


# TEST 15

def is_admissible_1_getargs():
    return [NEWGRAPH1, "H"]


def is_admissible_1_testanswer(val, original_val=None):
    return False == bool(val)


make_test(type='FUNCTION',
          getargs=is_admissible_1_getargs,
          testanswer=is_admissible_1_testanswer,
          expected_val='False for NEWGRAPH1/H',
          name='is_admissible')


# TEST 16

def is_admissible_2_getargs():
    return [NEWGRAPH1, "A"]


def is_admissible_2_testanswer(val, original_val=None):
    return True == bool(val)


make_test(type='FUNCTION',
          getargs=is_admissible_2_getargs,
          testanswer=is_admissible_2_testanswer,
          expected_val='True for NEWGRAPH1/A',
          name='is_admissible')


# TEST 17

def is_admissible_3_getargs():
    return [NEWGRAPH1, "C"]


def is_admissible_3_testanswer(val, original_val=None):
    return True == bool(val)


make_test(type='FUNCTION',
          getargs=is_admissible_3_getargs,
          testanswer=is_admissible_3_testanswer,
          expected_val='True for NEWGRAPH1/C',
          name='is_admissible')


# TEST 18

def is_admissible_4_getargs():
    return [NEWGRAPH1, "D"]


def is_admissible_4_testanswer(val, original_val=None):
    return False == bool(val)


make_test(type='FUNCTION',
          getargs=is_admissible_4_getargs,
          testanswer=is_admissible_4_testanswer,
          expected_val='False for NEWGRAPH1/D',
          name='is_admissible')


# TEST 19

def is_admissible_5_getargs():
    return [NEWGRAPH1, "E"]


def is_admissible_5_testanswer(val, original_val=None):
    return True == bool(val)


make_test(type='FUNCTION',
          getargs=is_admissible_5_getargs,
          testanswer=is_admissible_5_testanswer,
          expected_val='True for NEWGRAPH1/E',
          name='is_admissible')


# TEST 20

def is_consistent_1_getargs():
    return [NEWGRAPH1, "H"]


def is_consistent_1_testanswer(val, original_val=None):
    return False == bool(val)


make_test(type='FUNCTION',
          getargs=is_consistent_1_getargs,
          testanswer=is_consistent_1_testanswer,
          expected_val='False for NEWGRAPH1/H',
          name='is_consistent')


# TEST 21

def is_consistent_2_getargs():
    return [NEWGRAPH1, "A"]


def is_consistent_2_testanswer(val, original_val=None):
    return False == bool(val)


make_test(type='FUNCTION',
          getargs=is_consistent_2_getargs,
          testanswer=is_consistent_2_testanswer,
          expected_val='False for NEWGRAPH1/A',
          name='is_consistent')


# TEST 22

def is_consistent_3_getargs():
    return [NEWGRAPH1, "C"]


def is_consistent_3_testanswer(val, original_val=None):
    return True == bool(val)


make_test(type='FUNCTION',
          getargs=is_consistent_3_getargs,
          testanswer=is_consistent_3_testanswer,
          expected_val='True for NEWGRAPH1/C',
          name='is_consistent')


# TEST 23

def is_consistent_4_getargs():
    return [NEWGRAPH1, "D"]


def is_consistent_4_testanswer(val, original_val=None):
    return False == bool(val)


make_test(type='FUNCTION',
          getargs=is_consistent_4_getargs,
          testanswer=is_consistent_4_testanswer,
          expected_val='False for NEWGRAPH1/D',
          name='is_consistent')


# TEST 24

def is_consistent_5_getargs():
    return [NEWGRAPH1, "E"]


def is_consistent_5_testanswer(val, original_val=None):
    return True == bool(val)


make_test(type='FUNCTION',
          getargs=is_consistent_5_getargs,
          testanswer=is_consistent_5_testanswer,
          expected_val='True for NEWGRAPH1/E',
          name='is_consistent')
