class Solution:
  def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
    # Problem of type graph
    # build an adjacency list from the given information
    # apply DFS on the graph to find nodes are eventually safe

    # init a list that would act as an adj list
    adj_list = collections.defaultdict(list)
    # init a list that stores the number of outgoing links each node has
    outgoing_edges = []
    # init a list that would store the eventual safe nodes
    eventual_safe_nodes = []
    # init a queue
    queue = []
    for i in range(len(graph)):
      outgoing_edges.append(len(graph[i]))
      
      # if outgoing edges are not present
      if outgoing_edges[i] == 0:
        # add it to the queue
        queue.append(i)
      
      # build the adj list  
      for j in graph[i]: #
        adj_list[j].append(i) #

    print(adj_list)    
    # perform BFS iteratively
    while queue:
      node = queue.pop(0)
      # then place it in the eventual safe list
      eventual_safe_nodes.append(node)
      
      for n in adj_list[node]:
        outgoing_edges[n] -= 1
        # if you encounter a node with no outgoing links 
        if outgoing_edges[n] == 0:  
          queue.append(n)
      
    return sorted(eventual_safe_nodes)
