n=int(input())
adjDic={}
for i in range(n*n):
	if (i%n==0):
		adjDic[i]=list()
		adjDic[i].append(i+1)
		if (i+n<(n*n)):
			adjDic[i].append(i+n)
		if (i-n>=0):
			adjDic[i].append(i-n)
		if (i-(n-1)>=0):
			adjDic[i].append(i-(n-1))
		if (i+(n+1)<n*n):
			adjDic[i].append(i+n+1)
		
	elif (i%n==n-1):
		adjDic[i]=list()
		adjDic[i].append(i-1)
		if (i+n<(n*n)):
			adjDic[i].append(i+n)
		if (i-n>0):
			adjDic[i].append(i-n)
		if (i-(n+1)>0):
			adjDic[i].append(i-(n+1))
		if (i+(n-1)<n*n):
			adjDic[i].append(i+(n-1))
	else:
		if (i+n<n*n):
			adjDic[i]=list()
			adjDic[i].append(i+n)
		if (i-n>0):
			if adjDic.get(i):
				adjDic[i].append(i-n)
			else:
				adjDic[i]=list()
				adjDic[i].append(i-n)
		adjDic[i].append(i+1)
		adjDic[i].append(i-1)
		if (i-(n-1)>0):
			adjDic[i].append(i-(n-1))
		if (i+(n+1)<n*n):
			adjDic[i].append(i+n+1)
		if (i-(n+1)>=0):
			adjDic[i].append(i-(n+1))
		if (i+(n-1)<n*n):
			adjDic[i].append(i+(n-1))

# print(adjDic)
for i in adjDic:
	print(i,":",adjDic[i])
# stack=[0]
visited=set()
def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node,end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("dfs")
dfs(visited,adjDic,0)
print()


visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
print("bfs")
bfs(visited,adjDic,0)
print('\n')

from collections import deque

def color_graph_bfs(adj_matrix, num_colors):
    # Create a dictionary to store the colors assigned to each node
    node_colors = {}
    # Create a queue to hold the nodes to be processed
    node_queue = deque()
    # Start with the first node in the graph and assign it the first color
    start_node = next(iter(adj_matrix.keys()))
    node_colors[start_node] = 0
    node_queue.append(start_node)
    # Iterate over the remaining nodes using BFS
    while node_queue:
        current_node = node_queue.popleft()
        # Get the adjacent nodes for the current node
        adj_nodes = adj_matrix[current_node]
        # Initialize a set to store the colors already used by the adjacent nodes
        used_colors = set()
        # Iterate over each adjacent node and check its color (if assigned)
        for adj_node in adj_nodes:
            if adj_node in node_colors:
                used_colors.add(node_colors[adj_node])
            else:
                # Add uncolored adjacent nodes to the queue to be processed
                node_queue.append(adj_node)
        # Choose the first available color from the list of colors
        available_colors = set(range(num_colors)) - used_colors
        chosen_color = min(available_colors)
        # Assign the chosen color to the current node
        node_colors[current_node] = chosen_color
    return node_colors



color_dict=color_graph_bfs(adjDic,4)
count=1
for i in range(len(color_dict)):
	if (count%n==0):
		print(color_dict[i],end="\n")
		count=1
	else:
		print(color_dict[i],end=" ")
		count+=1	

def color_graph_dfs(adj_matrix, num_colors):
    # Create a dictionary to store the colors assigned to each node
    node_colors = {}
    # Start with the first node in the graph and assign it the first color
    start_node = next(iter(adj_matrix.keys()))
    dfs_coloring(adj_matrix, start_node, num_colors, node_colors)
    return node_colors

def dfs_coloring(adj_matrix, node, num_colors, node_colors):
    # Check if all nodes have been assigned a color
    if len(node_colors) == len(adj_matrix):
        return True
    
    # Get the adjacent nodes for the current node
    adj_nodes = adj_matrix[node]
    
    # Try each color for the current node
    for color in range(num_colors):
        # Check if the color is already used by adjacent nodes
        if any(node_colors.get(adj_node) == color for adj_node in adj_nodes):
            continue
        
        # Assign the color to the current node
        node_colors[node] = color
        
        # Recursively color the adjacent nodes
        all_colored = True
        for adj_node in adj_nodes:
            if adj_node not in node_colors:
                if not dfs_coloring(adj_matrix, adj_node, num_colors, node_colors):
                    all_colored = False
                    break
        
        # If all adjacent nodes can be colored, return True
        if all_colored:
            return True
        
        # Backtrack and try a different color
        del node_colors[node]
    
    # If all colors have been tried and none work, return False
    return False


print()
color_dict=color_graph_dfs(adjDic,4)
count=1
for i in range(len(color_dict)):
	if (count%n==0):
		print(color_dict[i],end="\n")
		count=1
	else:
		print(color_dict[i],end=" ")
		count+=1
