class MinStack(object):

    def __init__(self):
        self.min = float('inf')
        self.stack = []
        
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.min = min(self.min, val)
        self.stack.append((self.min, val))
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min = self.stack[-1][0] if self.stack else float('inf')
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
