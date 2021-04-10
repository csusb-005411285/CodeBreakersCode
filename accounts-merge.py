#Concise
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj_list = defaultdict(list)
        email_map = defaultdict(str)
        visited = set()
        merged_accounts = defaultdict(list)
        for i, account in enumerate(accounts):
            for j, email in enumerate(account[1:], start = 1): 
                email_map[email] = account[0]
                for k in range(1, len(account)):
                    adj_list[email].append(account[k])
        for i, account in enumerate(accounts):
            for j, email in enumerate(account[1:], start = 1):
                if email not in visited:
                    merged_accounts[email] = self._accounts_merge(adj_list, visited, email, [])
        for key, value in merged_accounts.items():
            merged_accounts[key].sort()
            merged_accounts[key].insert(0, email_map[key])
        return merged_accounts.values()
    
    def _accounts_merge(self, adj_list, visited, email, path):
        if email in visited:
            return path
        visited.add(email)
        path.append(email)
        for neigh in adj_list[email]:
            self._accounts_merge(adj_list, visited, neigh, path)
        return path
    
# Recursive
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj_list = defaultdict(set)
        self.build_graph(accounts, adj_list)
        visited = set()
        merged_accounts = []
        for i, account in enumerate(accounts):
            connected_accounts = []
            results = []
            for j, detail in enumerate(account):
                if j == 0:
                    results.append(detail)
                    continue
                if detail not in visited:
                    connected_accounts = self._accounts_merge(accounts, adj_list, visited, detail)
                    for acc in sorted(connected_accounts):
                        results.append(acc)
            if len(results) > 1:
                merged_accounts.append(results)
        return merged_accounts

    def build_graph(self, accounts, adj_list):
        for i, account in enumerate(accounts):
            emails = account[1:]
            for j in range(len(emails)):
                if j + 1 < len(emails):
                    curr_email = emails[j]
                    next_email = emails[j + 1]
                    adj_list[curr_email].add(next_email)
                    adj_list[next_email].add(curr_email)

    def _accounts_merge(self, accounts, graph, visited, vert):
        if vert in visited:
            return []
        visited.add(vert)
        connected_accounts = []
        connected_accounts.append(vert)
        for neighbor in graph[vert]:
            for account in self._accounts_merge(accounts, graph, visited, neighbor):
                connected_accounts.append(account)
        return connected_accounts

class Solution:
    def accountsMerge(self, accounts: [[str]]) -> [[str]]:
        graph = defaultdict(set)
        email_name = defaultdict(str)
        merged_accounts = []
        for acc in accounts:
            emails = acc[1:]
            for email in emails:
                graph[emails[0]].add(email)
                graph[email].add(emails[0])
        for acc in accounts:
            emails = acc[1:]
            name = acc[0]
            for i in range(len(emails)):
                email_name[emails[i]] = name
        visited = set()
        for email in graph:
            stack = defaultdict(list)
            stack = [email]
            connected_emails = []
            while stack:
                email = stack.pop()
                if email in visited:
                    continue
                connected_emails.append(email)
                visited.add(email)
                neighbors = graph[email]
                for neigh in neighbors:
                    stack.append(neigh)
            if connected_emails:
                merged_accounts.append([email_name[email]] + sorted(connected_emails)) 
        return merged_accounts
