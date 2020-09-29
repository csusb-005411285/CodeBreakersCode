class Solution:
    def __init__(self):
        self.parent = [i for i in range(26)]

    def find_parent(self, vert):
        if self.parent[vert] == vert: 
            return vert

        return self.find_parent(self.parent[vert])

    def equationsPossible(self, equations: [str]) -> bool:

        for i in equations:
            
            a = ord(i[0]) - ord('a')
            b = ord(i[3]) - ord('a')
            eq = i[1]

            pa = self.find_parent(a)
            pb = self.find_parent(b)

            if eq == '=':
                if pa != pb: 
                    self.parent[pb] = pa

        for i in equations:
            
            a = ord(i[0]) - ord('a')
            b = ord(i[3]) - ord('a')
            eq = i[1]

            pa = self.find_parent(a)
            pb = self.find_parent(b)

            if eq == '!':
                if pa == pb:
                    return False

        return True
