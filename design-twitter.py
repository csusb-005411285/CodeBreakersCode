class Tweet:
    clock = 0

    def __init__(self, id):
        self.tweet_id = id 
        self.timestamp = Tweet.clock
        Tweet.clock += 1

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = defaultdict(deque)
        self.followers = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].append(Tweet(tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        news = []
        news_feed = []
        self.get_recent_tweets(news, userId)
        for follower in self.followers[userId]:
            if userId == follower: continue
            self.get_recent_tweets(news, follower)
        count = 0
        while news and count < 10:
            news_feed.append(heappop(news)[1])
            count += 1
        return news_feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId: return
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        
    def get_recent_tweets(self, news, userId):
        for i in range(len(self.tweets[userId])):
            tweet = self.tweets[userId][i]
            tweet_id = tweet.tweet_id
            timestamp = tweet.timestamp
            heappush(news, (-timestamp, tweet_id))
   
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
