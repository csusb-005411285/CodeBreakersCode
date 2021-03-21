class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree_list = defaultdict(int)
        visited = set()
        stack = []
        for i in range(n):
            indegree_list[i] = 0
        for left, right in zip(leftChild, rightChild):
            if left > -1:
                indegree_list[left] += 1
            if right > -1:
                indegree_list[right] += 1
        for key, val in indegree_list.items():
            if val > 1:
                return False
            if val == 0:
                stack.append(key)
        if len(stack) > 1:
            return False
        while stack:
            node = stack.pop()
            if node in visited:
                return False
            visited.add(node)
            if leftChild[node] > -1:
                left_child_node = leftChild[node]
                indegree_list[left_child_node] -= 1
                if indegree_list[left_child_node] == 0:
                    stack.append(left_child_node)
            if rightChild[node] > -1:
                right_child_node = rightChild[node]
                indegree_list[right_child_node] -= 1
                if indegree_list[right_child_node] == 0:
                    stack.append(right_child_node)
        return len(visited) == len(indegree_list)
