class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

def color_graph(graph, colors):
    # Create a valid coloring for the graph
    for k, vert in enumerate(graph):
        neigh_colors = set()
        if vert in vert.neighbors: raise Exception('The graph has a loop.')
        for neighbor in vert.neighbors:
            neigh_colors.add(neighbor.color)
        for color in colors:
            if color not in neigh_colors:
                vert.color = color
                break
    return 0
