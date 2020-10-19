def diskStacking(disks):
    if not disks:
        return []
    if len(disks) == 1:
        return disks
    disks.sort(key=lambda x: x[2])
    heights = [x[2] for x in disks]
    sequences = [None for _ in range(len(disks)) ]
    for i in range(1, len(disks)):
        max_height = 0
        for j in range(0, i):
            if disks[j][0] < disks[i][0] and disks[j][1] < disks[i][1] and disks[j][2] < disks[i][2]:
                heights[i] = max(heights[i], disks[i][2] + heights[j])
                if heights[i] > max_height:
                    max_height = heights[i]
                    sequences[i] = j
    max_val = max(heights)
    max_val_index = heights.index(max_val)
    return build_sequence(sequences, disks, max_val_index)

def build_sequence(seq, disks, index):
    res = []
    while index is not None:
        res.append(disks[index])
        index = seq[index] 
    return list(reversed(res))
