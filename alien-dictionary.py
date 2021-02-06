class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj_list = defaultdict(set)
        indegree_list = defaultdict(int)
        stack = deque()
        order_of_letters = ''
        visited = set()
        for i, word in enumerate(words):
            for j, char in enumerate(word):
                indegree_list[char] = 0
        for i in range(len(words)-1):
            for source, dest in zip(words[i], words[i+1]):
                if source!=dest:
                    if dest not in adj_list[source]:
                        adj_list[source].add(dest)
                        indegree_list[dest] += 1   
                    break
            else:
                if len(words[i+1]) < len(words[i]):
                    return ''
        for vert, indegree in indegree_list.items():
            if indegree == 0:
                stack.append(vert)
        while stack:  
            vert = stack.pop()
            if vert in visited:
                return ''
            visited.add(vert)
            order_of_letters += vert
            for neighbor in adj_list[vert]:
                indegree_list[neighbor] -= 1
                if indegree_list[neighbor] == 0:
                    stack.append(neighbor)
        return order_of_letters if len(order_of_letters) == len(indegree_list) else ''
