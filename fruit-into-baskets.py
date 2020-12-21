class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        left = 0
        right = 0
        max_len = 0
        fruit_map = defaultdict(int)
        for right, fruit in enumerate(tree):
            fruit_map[fruit] += 1
            while len(fruit_map.keys()) > 2 and left < right:
                fruit_type = tree[left]
                fruit_map[fruit_type] -= 1
                if fruit_map[fruit_type] == 0: del fruit_map[fruit_type]
                left += 1
            max_len = max(max_len, sum(fruit_map.values()))
        return max_len
