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
