class Solution:
    def solve(self, contacts):
        if not contacts:
            return 0
        duplicates_count = 0
        contact_dict = defaultdict(int)
        for i in range(len(contacts)):
            found = False
            for j in range(len(contacts[i])):
                if contacts[i][j] in contact_dict and not found:
                    duplicates_count += 1
                    found = True
                contact_dict[contacts[i][j]] += 1
        return len(contacts) - duplicates_count
