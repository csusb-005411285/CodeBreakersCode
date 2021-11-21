class Leaderboard:

    def __init__(self):
        self.leaderboard = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.leaderboard[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        scores = 0
        for player_id, score in self.leaderboard.items():
            heappush(heap, (-score))
        while K:
            scores += -heappop(heap)
            K -= 1
        return scores

    def reset(self, playerId: int) -> None:
        del self.leaderboard[playerId]
