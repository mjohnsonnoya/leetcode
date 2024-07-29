class Twitter:

    def __init__(self):
        self.followmap = defaultdict(set)
        self.tweetmap = defaultdict(list)
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append((self.t, tweetId))
        self.t -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        ans = []
        self.followmap[userId].add(userId)
        for followee in self.followmap[userId]:
            print("iteration: ",followee)
            if self.tweetmap[followee]:
                index = len(self.tweetmap[followee]) - 1
                time, tweetId = self.tweetmap[followee][index]
                heapq.heappush(heap,(time, tweetId, index - 1, followee))
        while len(ans) < 10 and heap:
            time, tweetId, index, followeeId = heapq.heappop(heap)
            ans.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweetmap[followeeId][index]
                heapq.heappush(heap, (time, tweetId, index - 1, followeeId))
            
        return ans
            


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
