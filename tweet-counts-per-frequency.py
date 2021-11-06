class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)
        
    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        seconds = 60
        if freq == 'hour':
            seconds = 3600
        elif freq == 'day':
            seconds = 86400
        chunks = ((endTime - startTime)//seconds) + 1
        time_chunks = [0] * chunks
        for time in self.tweets[tweetName]:
            if startTime <= time <= endTime: # 2.
                index = (time-startTime)//seconds # 1.
                time_chunks[index] += 1
        return time_chunks
    
'''
1. the time is relative to the start time
2. the time should be between the start time and end time
'''
