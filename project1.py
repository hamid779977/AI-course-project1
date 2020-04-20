# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation
from search import Graph


def bfs(graph, start, goal):
    # Your Code Here
    raise NotImplementedError
   

# Once you have completed the breadth-first search,
# this part should be very simple to complete.
def dfs(graph, start, goal):
	flag=0
	print("goal:"+goal)
	print("start:"+start)
	visited =[]
	l= graph.get_connected_nodes(start)
	for index in range(len(l)):
		visited.append(l[index])
		l[index]=l[index]+start
		
	while len(l)>0 and flag==0:
		ind=len(l)-1
		s=l[ind]
		l.pop(ind)
		t=graph.get_connected_nodes(s[0])
		for index in range(len(t)):
			if(t[index] not in visited):
				s=t[index]+s
				print(s)
				l.append(s)
				visited.append(t[index])
				
				if s[0]==goal:
					flag=1
					print("answer")
					print(s)



			
	
	exit()	



    # Your Code Here
     #l= graph.get_connected_nodes(start)

     #while len(l)>0 :

		 #ind = len(l)-1
		 #s=l[ind]
	     #s=s+s     	
		# l.pop(ind)
     		
     #	count=len(s)-1
     #	t = graph.get_connected_nodes(s[0])
     #	for x in xrange(1,10):
     #		pass
     #	for index in range(len(t)):
  	#		s=t[index] + s
  	#		print(s)
  	#		print(type(s))
    #		 l.append(s)

    	#	  if s[0]=goal:
    	#	  		flag=true

     	
  					
     	  	
  		  
  		  
  		  	
  		  	


# Now we're going to try optimal search.  The previous searches haven't
# used edge distances in the calculation.

# This function takes in a graph and a list of node names, and returns
# the sum of edge lengths along the path -- the total distance in the path.

def path_length(graph, node_names):
    for index in range(len(node_names)):
  		  print('node:', node_names[index])


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
