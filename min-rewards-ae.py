# tc: o(n2), sc: o(n)
def minRewards(scores):
    if len(scores) == 1:
        return 1 

    if len(scores) == 2:
        return 3

    local_minimas = get_local_minima(scores)
    results = get_scores(scores, local_minimas)
    return sum(results)

def get_local_minima(scores):
    minimas = []
    for i in range(len(scores) - 1):
        if i == 0 and scores[i] < scores[i + 1]:
            minimas.append(i)
        elif i == len(scores) - 1 and scores[i] < scores[i - 1]:
            minimas.append(i)
        elif scores[i] < scores[i + 1] and scores[i] < scores[i - 1]:
            minimas.append(i)
    return minimas

def get_scores(scores, minimas):
    results = [1 for _ in range(len(scores))]
    for j in minimas:
        forward = j + 1
        backward = j - 1
        
        while backward >= 0 and scores[backward] > scores[backward + 1]:
            results[backward] = max(results[backward], results[backward + 1] + 1)
            backward -= 1

        while forward < len(scores) and scores[forward] > scores[forward - 1]:
            results[forward] = results[forward - 1] + 1
            forward += 1
    
    return results 
