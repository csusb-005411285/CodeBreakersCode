class Solution:
    def __init__(self):
        self.min = float('inf')
    
    def minStickers(self, stickers: List[str], target: str) -> int:
        target_map = Counter(target)
        res = float('inf')
        sticker_map = defaultdict(int)
        self._min_stickers(stickers, target, target_map, 0, 0, res, sticker_map)
        return self.min if self.min != float('inf') else -1
    
    def _min_stickers(self, stickers, target, char_map, used, i, res, sticker_map):
        if used + 1 > self.min: 
            return
        if i > len(target):
            return
        if i == len(target):
            self.min = min(self.min, used)
            return
        if target[i] in sticker_map and sticker_map[target[i]] >= char_map[target[i]]:
            self._min_stickers(stickers, target, char_map, used, i + 1, res, sticker_map)
        for j, sticker in enumerate(stickers):
            if target[i] in sticker:
                for s in sticker:
                    sticker_map[s] += 1
                self._min_stickers(stickers, target, char_map, used + 1, i, res, sticker_map)
                for s in sticker:
                    sticker_map[s] -= 1
        return
