class Solution:
  def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
    graph_len = len(graph)
    # init a list to store the outgoing edges from the node
    edges = [0] * graph_len
    # init a dict to store the adjacency list
    adj_list = collections.defaultdict(list) 
    # init a queue
    queue = []
    ret = []
    # loop through the graph
    for i in range(graph_len):
        # store the number of outgoing edges from each node
        edges[i] = len(graph[i])
        # if leaf node
        if edges[i]==0:
            # add it to the queue
            queue.append(i)
        # associate each node with the node connected to it.
        # create an adjacency list
        for j in graph[i]:
          adj_list[j].append(i)
    
    # loop through the queue
    while queue:
      # pop the first node
      term_node = queue.pop(0)
      # store it in the results list
      ret.append(term_node)
      # loop through the adjacency list
      # when you remove the terminal node, all the nodes connected to the
      # terminal node become the new terminal nodes
      for node in adj_list[term_node]:
        # reduce the length of outgoing edges from the node 
        edges[node] -= 1
        # if we encounter a terminal node 
        if edges[node]==0:
          # add it to the queue
          queue.append(node)
    # return thhe sotred array
    return sorted(ret)
