class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        adj_list = defaultdict(list)
        res = []
        heap = []
        min_dist = [[float('inf') for _ in range(len(targetPath))] for _ in range(n)]
        prev_vert = [[None for _ in range(len(targetPath))] for _ in range(n)]
        # build graph
        for road in roads:
            src, dest = road
            adj_list[src].append(dest)
            adj_list[dest].append(src)
        # populate matrices
        for row in range(len(min_dist)):
            if names[row] == targetPath[0]:
                min_dist[row][0] = 0
            else:
                min_dist[row][0] = 1
        # Dijkastras
        for row in range(len(min_dist)):
            heappush(heap, (min_dist[row][0], row, 0))
        final_city_index = None
        while heap:
            dist, names_index, target_path_index = heappop(heap)
            if target_path_index == len(targetPath) - 1:
                final_city_index = names_index
                break
            next_index = target_path_index + 1
            for neigh_index in adj_list[names_index]:
                next_dist = dist
                if names[neigh_index] != targetPath[next_index]:
                    next_dist += 1
                if next_dist < min_dist[neigh_index][next_index]:
                    min_dist[neigh_index][next_index] = next_dist
                    prev_vert[neigh_index][next_index] = names_index
                    heappush(heap, (next_dist, neigh_index, next_index))
        # build the path
        res = [final_city_index]
        target_index = len(targetPath) - 1
        name_index = final_city_index
        while prev_vert[name_index][target_index] is not None:
            name_index = prev_vert[name_index][target_index]
            res.append(name_index)
            target_index -= 1
        # return
        return res[::-1]
