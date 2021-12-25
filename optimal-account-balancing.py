class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        adj_list = defaultdict(int)
        visited = set()
        for transaction in transactions:
            _from, to, amt = transaction
            adj_list[_from] -= amt
            adj_list[to] += amt
        debts = [amt for amt in adj_list.values() if amt != 0]
        return self.find_min_num_transactions(adj_list, visited, debts, 0)
    
    def find_min_num_transactions(self, adj_list, visited, debts, i):
        while i < len(debts) and debts[i] == 0:
            i += 1
        if i == len(debts):
            return 0
        min_transactions = float('inf')
        for j in range(i + 1, len(debts)):
            if debts[i] * debts[j] < 0:
                debts[j] += debts[i]
                min_transactions = min(min_transactions, self.find_min_num_transactions(adj_list, visited, debts, i + 1) + 1)
                debts[j] -= debts[i]
                visited.add(debts[j])
        return min_transactions
