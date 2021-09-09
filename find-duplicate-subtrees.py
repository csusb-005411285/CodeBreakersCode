class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # init vars
        duplicate_subtrees = []
        node_map = defaultdict(int)
        # call recursive method
        self.find_duplicate_subtrees(root, node_map)
        # find all values in the list that have a count > 1
        for key, values in node_map.items():
            if values[1] > 1:
                duplicate_subtrees.append(values[0])
        # return
        return duplicate_subtrees
    
    def find_duplicate_subtrees(self, node, node_map):
        # base case
        # if null
        if not node:
            return 'null'
        # if leaf
        # if not node.left and not node.right:
        #     return str(node.val)
        # move left
        left = self.find_duplicate_subtrees(node.left, node_map)
        # move right
        right = self.find_duplicate_subtrees(node.right, node_map)
        # process node
        # generate key
        key = 'l' + left + ',' + str(node.val) + ',' + right + 'r'
        # add to hash map
        if key in node_map:
            node_map[key][1] += 1
        else:
            node_map[key] = [node, 1]
        # return key
        return key
