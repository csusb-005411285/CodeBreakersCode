def get_path(graph, start_node, end_node):
    if start_node not in graph or end_node not in graph:
        raise Exception('Source or destination not found')
        
    visited = build_visited_map(graph)
    path = {} 
    route = []
    path = get_path_helper(graph, start_node, end_node, visited, path)
    get_route(path, end_node, route)
    if not route:
        return None
    return list(reversed(route))

def get_route(path, end_node, route=[]):
    if end_node not in path:
        return route 
    route.append(end_node)
    while path[end_node] and path[end_node] != '*':
        route.append(path[end_node])
        end_node = path[end_node]
    return route 

def build_visited_map(graph):
    visited = {}
    for key in graph:
        visited[key] = False 
    return visited

def get_path_helper(graph, start_node, end_node, visited, path):
    if start_node not in graph:
        raise Exception('Cannot find the start node')

    queue = deque()
    queue.append(['*', start_node])
    
    while queue:
        _from, to = queue.popleft()
        
        if visited[to]:
           continue
        
        if to == end_node:
            path[to] = _from 
            return path 

        visited[to] = True
        path[to] = _from

        for neighbor in graph[to]:
            queue.append([to, neighbor]) 

    return path 
