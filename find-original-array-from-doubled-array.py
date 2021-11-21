class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        original = []
        if len(changed) % 2 != 0:
            return []
        changed.sort()
        changed_freq_map = Counter(changed)
        for num in changed:
            if num in changed_freq_map:
                changed_freq_map[num] -= 1
                if changed_freq_map[num] == 0:
                    del changed_freq_map[num]
                if num + num in changed_freq_map:
                    original.append(num)
                    changed_freq_map[num + num] -= 1
                    if changed_freq_map[num + num] == 0:
                        del changed_freq_map[num + num]
                else:
                    return []
        return original
