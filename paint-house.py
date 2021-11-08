class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        cache = defaultdict(int)
        return min(self.get_min_cost(costs, 0, 0, cache), self.get_min_cost(costs, 0, 1, cache), self.get_min_cost(costs, 0, 2, cache))
    
    def get_min_cost(self, costs, i, color, cache):
        if (i, color) in cache:
            return cache[(i, color)]
        if i == len(costs):
            return 0
        cost_painting_red = float('inf')
        cost_painting_green = float('inf')
        cost_painting_blue = float('inf')
        if color == 0:
            cost_painting_red = costs[i][color] + min(self.get_min_cost(costs, i + 1, 1, cache), self.get_min_cost(costs, i + 1, 2, cache))
        elif color == 1:
            cost_painting_green = costs[i][color] + min(self.get_min_cost(costs, i + 1, 0, cache), self.get_min_cost(costs, i + 1, 2, cache))
        elif color == 2:
            cost_painting_blue = costs[i][color] + min(self.get_min_cost(costs, i + 1, 0, cache), self.get_min_cost(costs, i + 1, 1, cache))
        cache[(i, color)] = min(cost_painting_red, cost_painting_green, cost_painting_blue)
        return min(cost_painting_red, cost_painting_green, cost_painting_blue)
