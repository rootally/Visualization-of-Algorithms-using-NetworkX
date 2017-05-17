import networkx as nx
import matplotlib.pyplot as plt
#----------------------------------------------------------------------
Dfs=[]
def get_matrix(n):
   """Read in and return a matrix of ints with n rows and n columns"""
   mat = []
   print "Enter the rows of the matrix, one row per line"
   for i in range(n):
      row_str = raw_input("")
      row_str_l = row_str.split()
      row = []
      for j in range(n):
         row.append(int(row_str_l[j]))
      mat.append(row)
   return mat

#----------------------------------------------------------------------
def print_matrix(mat, n):
   """Print a matrix with n rows and n columns"""
   for i in range(n):
      for j in range(n):
         print mat[i][j],
      print

#----------------------------------------------------------------------
def all_false(n):
   """Create a list, all of whose elements are False"""
   visited = []
   for i in range(n):
      visited.append(False)
   return visited

#----------------------------------------------------------------------
def print_list(l):
   """Print the contents of a list"""
   for i in l:
      print i,
   print

#----------------------------------------------------------------------
def depth_first_search(vert, mat, visited, n):
   """Visit the vertices in the digraph using depth-first search"""
   global Dfs
   
   Dfs.append(vert)
   ##print "Visiting", vert
    
   visited[vert] = True
   for i in range(n):
      if mat[vert][i] == 1 and not visited[i]:
             depth_first_search(i, mat, visited, n)

#----------------------------------------------------------------------
n = int(raw_input("How many vertices\n   "))
mat = get_matrix(n)
print
print_matrix(mat, n)

visited = all_false(n)

print
depth_first_search(0, mat, visited, n)
#calling the DFS function to get the traversal order!

G = nx.Graph()
#Creating the Graph

for i in xrange(n):
	for j in xrange(n):
		if mat[i][j]>0:
			G.add_edge(i,j,W=mat[i][j])  #Building the Graph, where W is the Weight
				
edge = list(nx.dfs_edges(G,0))

pos=nx.spring_layout(G,k=1,iterations= 20) # positions for all nodes

print ('The DFS Order Traversal')
print Dfs
nx.draw(G,pos)
nx.draw_networkx_nodes(G,pos,node_size=700) #Drawing the nodes of graph G
nx.draw_networkx_edges(G,pos,edgelist=edge,width=6) #Drawing the edges of thr Graph as per the DFS order
nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')# Drawing the labels of the Graph
nx.draw_networkx_edge_labels(G,pos,font_size=12,font_family='sans-serif')# Drawing the weights!

plt.show() # A matplotlib function to plot the Graph 

