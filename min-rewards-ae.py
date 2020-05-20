def minRewards(scores):
    if len(scores) == 1:
        return 1

    local_minima_index = find_local_minimas(scores)
    scores = get_scores_from_minimas(scores, local_minima_index)
    return sum(scores)

def get_scores_from_minimas(scores, index):
    results = [0 for _ in range(len(scores))] 

    for i in index:
        forward = i
        backward = i
        results[i] = 1

        while backward >= 0:
            if scores[backward - 1] > scores[backward]:
                results[backward - 1] = max(results[backward - 1], results[backward] + 1)
                backward -= 1
            else:
                break
          
        while forward < len(scores) - 1 and i != len(scores) - 1:
            if scores[forward + 1] > scores[forward]:
                results[forward + 1] = max(results[forward + 1], results[forward] + 1) 
                forward += 1
            else:
                break
    
    return results

def find_local_minimas(scores):
    results = []
    for i in range(len(scores)):
        if i == 0 and scores[i] < scores[i + 1]:
            results.append(i)
        elif i == len(scores) - 1 and scores[i] < scores[i - 1]:
            results.append(i)
        elif scores[i] < scores[i - 1] and scores[i] < scores[i + 1]:
            results.append(i)
    return results
