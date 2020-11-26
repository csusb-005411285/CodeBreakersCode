# Input is a list
class Solution():
    def find_max_cpu_load(self, jobs):
        jobs.sort(key = lambda x: x[0])
        max_load = jobs[0][2]
        curr_load = jobs[0][2]
        heap = []
        heap.append((jobs[0][1], jobs[0]))
        for i, job in enumerate(jobs[1:], start=1):
            if job[0] < heap[0][1][1]:
                    heappush(heap, (job[1], job))
                    curr_load += job[2]
                    max_load = max(max_load, curr_load)
            else:
                while heap and heap[0][1][1] < job[0]:
                    heappop(heap)
                heappush(heap, (job[1], job))
                curr_load = job[2]
                max_load = max(max_load, curr_load)
        return max_load
    
class job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        return self.end < other.end 

def find_max_cpu_load(jobs):
    overlapping_intervals = []
    jobs.sort(key=lambda x: x.start)
    overlapping_intervals.append(jobs[0])
    curr_cpu_load = jobs[0].cpu_load
    max_cpu_load = jobs[0].cpu_load
    for job in jobs[1:]:
        if job.start < overlapping_intervals[0].end:
            heappush(overlapping_intervals, job)
            curr_cpu_load += job.cpu_load
        else:
            while overlapping_intervals and job.start >= overlapping_intervals[0].end:
                removed_job = heappop(overlapping_intervals)
                curr_cpu_load -= removed_job.cpu_load
            heappush(overlapping_intervals, job)
            curr_cpu_load += job.cpu_load
        max_cpu_load = max(max_cpu_load, curr_cpu_load)
    return max_cpu_load 
