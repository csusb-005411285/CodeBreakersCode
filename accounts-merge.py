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
