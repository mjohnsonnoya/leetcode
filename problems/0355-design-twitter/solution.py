class Twitter:

    def __init__(self):
        self.tweetmap = defaultdict(list)
        self.followingmap = defaultdict(set)
        self.count = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minheap = []
        res = []
        self.followingmap[userId].add(userId)
        for followeeId in self.followingmap[userId]:
            if followeeId in self.tweetmap:
                index = len(self.tweetmap[followeeId]) - 1
                count, tweetId = self.tweetmap[followeeId][index]
                heapq.heappush(minheap, (count, tweetId, index - 1, followeeId))
        while minheap and len(res) < 10:
            count, tweetId, index, followeeId = heapq.heappop(minheap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetmap[followeeId][index]
                heapq.heappush(minheap, (count, tweetId, index - 1, followeeId))
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followingmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followingmap[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
