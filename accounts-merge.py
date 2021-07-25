#Concise
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_name = defaultdict(str)
        adj_list = defaultdict(list)
        res = []
        visited = set()
        # build graph
        # loop through accounts
        for acct in accounts:
            name = acct[0]
            for val in acct[1:]:
                # connect first email to all other emails
                adj_list[acct[1]].append(val)
                # connect all emails to the first email
                adj_list[val].append(acct[1])
                # update email_name map
                email_name[val] = name
            
        # perform dfs
        # loop through graph
        for src, dest in adj_list.items():
            # if vert is not visited
            if src not in visited:
                # perform dfs
                components = self.get_connected_components(adj_list, src, visited)
                
                # build the result
                # sort the result
                components.sort()
                # add name as the first entry in the list
                components.insert(0, email_name[components[0]])
                # add to res
                res.append(components)
        return res
    
    def get_connected_components(self, adj_list, vert, visited):
        # if visited
        if vert in visited:
            return []
        # add to visited
        visited.add(vert)
        components = [vert]
        # get neighbors
        for neigh in adj_list[vert]:
            # call recursive method
            nodes = self.get_connected_components(adj_list, neigh, visited)
            # store results of recursive method
            for node in nodes:
                components.append(node)
        return components
    
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
