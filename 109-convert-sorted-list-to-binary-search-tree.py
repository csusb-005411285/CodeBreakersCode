class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        return self.sorted_list_to_bst_helper(head)
    
    def sorted_list_to_bst_helper(self, node):
        if not node:
            return None
        
        if not node.next:
            return TreeNode(node.val)

        mid = self.find_mid_of_list(node)
        mnode = TreeNode(mid.val)
        mnode.left = self.sorted_list_to_bst_helper(node)
        mnode.right = self.sorted_list_to_bst_helper(mid.next)

        return mnode        

    def find_mid_of_list(self, node):
        prev = None
        slow = node
        fast = node

        while fast and fast.next:
            fast = fast.next.nextt:
            prev = slow
            slow = slow.next
        
        if prev:
            prev.next = None
        
        return slow

