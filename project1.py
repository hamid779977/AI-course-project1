# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation
from search import Graph
import operator

def bfs(graph, start, goal):
	flag=0
	print("goal: b   f  s"+goal)
	print("start:"+start)
	visited =[start]

	l=[start]
		
	while len(l)>0 and flag==0:
		ind=len(l)-1
		s=l[0]
		l.pop(0)
		t=graph.get_connected_nodes(s[0])
		
		for index in range(len(t)):

			if(t[index] not in visited):
				g=t[index]+s
				
				l.append(g)
				print(l)
				visited.append(t[index])
				
				if g[0]==goal:
					flag=1
					
					print(g)

	
    # Your Code Here
   
	   

# Once you have completed the breadth-first search,
# this part should be very simple to complete.
def dfs(graph, start, goal):
	#print( graph.get_connected_nodes('B'))
	flag=0
	print("goal:"+goal)
	print("start:"+start)
	visited =[start]

	l=[start]
		
	while len(l)>0 and flag==0:
		ind=len(l)-1
		s=l[ind]
		l.pop(ind)
		t=graph.get_connected_nodes(s[0])
		
		for index in range(len(t)):

			if(t[index] not in visited):
				g=t[index]+s
				
				l.append(g)
				print(l)
				visited.append(t[index])
				
				if g[0]==goal:
					flag=1
					
					print(g)

		
			
	uniform_cost_search(graph, start, goal)

	return 0				
	

  		  	


# Now we're going to try optimal search.  The previous searches haven't
# used edge distances in the calculation.

# This function takes in a graph and a list of node names, and returns
# the sum of edge lengths along the path -- the total distance in the path.

def path_length(graph, node_names):
	for x in range(len(node_names)):
		
		exit()	
    


def uniform_cost_search(graph, start, goal):
    # Your Code Here

    Queue=[(start,0)]
    Expanded=[]
    flag=0
    while len(Queue) > 0 and flag==0:
    	
    	#sort queue
    	#print(len(Queue))
    #	print(Queue[0][0])
    	s=Queue[0][0]
    	length=Queue[0][1]
    	Expanded.append(s)
    	Queue.pop(0)
    	connect_graph=graph.get_connected_nodes(s[0])
    	for index in range(len(connect_graph)):
    		k=graph.get_edge(connect_graph[index],s[0]).node2
    	#	print(k)
    		if k not in Expanded:
    			j=graph.get_edge(connect_graph[index],s[0]).length
    			k=k+s
    			temp=(k,j+length)
    			Queue.append(temp)
    			print(Queue)

    	Queue.sort(key=lambda x:x[1])		
    	if Queue[0][0][0]==goal:
    		flag=1
    		




    print(Queue[0])			

	   		

   # connect_graph=graph.get_connected_nodes(start)
  #  for index in range(len(connect_graph[0])):
   # 	k=graph.get_edge(connect_graph[index], start).node2
    #	j=graph.get_edge(connect_graph[index], start).length
    #	Expanded.append(k)
    #	Queue.update({k:j})
    #	print(Queue)
    """
    while len(Queue)>0:
    	ind = len(Queue)
    	s=graph.get_edge(connect_graph[ind], start).node2
    	count=graph.get_edge(connect_graph[index], start).length
    	t=graph.get_connected_nodes(s[0])
    	del Queue[k]
    	for index in range(len(t)):
    		if t[index] not in Expanded:
    			k=graph.get_edge(connect_graph[index], start).node2
   			 	j=graph.get_edge(connect_graph[index], start).length


"""
    			
    		

    	
    	
    
    



def a_star(graph, start, goal):
	print("here")
    # Your Code Here
    


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
