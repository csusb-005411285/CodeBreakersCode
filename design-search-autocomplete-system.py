class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.count = defaultdict(int)

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.current_search_term = ''
        self.curr_root = self.root
        for i, sentence in enumerate(sentences):
            self.add(sentence, times[i])
        
    def add(self, sentence, count):
        curr = self.root
        for char in sentence:
            curr = curr.children[char] # 1. 
            curr.count[sentence] += count # 2.
            
    def input(self, c: str) -> List[str]:
        search_results = []
        heap = []
        k = 3
        if c == '#':
            self.add(self.current_search_term, 1)
            self.current_search_term = ''
            self.curr_root = self.root
            return []
        self.current_search_term += c
        self.curr_root = self.curr_root.children[c]
        for sentence, count in self.curr_root.count.items():
            heappush(heap, (-count, sentence))
        while heap and k:
            count, sentence = heappop(heap)
            search_results.append(sentence)
            k -= 1
        return search_results

'''
1. Assigns the current char as the child of the current object.
2. Increment the count on the children and not on the current node.
'''
