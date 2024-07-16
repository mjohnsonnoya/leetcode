import heapq
from time import time

class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1  # Decrement to ensure the latest tweet has the smallest timestamp

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        self.following[userId].add(userId)
        for followee in self.following[userId]:
            if followee in self.tweets:
                index = len(self.tweets[followee]) - 1
                count, tweetId = self.tweets[followee][index]
                heapq.heappush(heap, [count, tweetId, followee, index - 1])
        while heap and len(res) < 10:
            count, tweetId, followee, index = heapq.heappop(heap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweets[followee][index]
                heapq.heappush(heap,[count, tweetId, followee, index - 1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId, tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId, followeeId)
# obj.unfollow(followerId, followeeId)

