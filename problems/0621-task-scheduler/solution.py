class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26
        for task in tasks:
            counts[ord(task) - ord("A")] -= 1

        heap = []
        for count in counts:
            if count != 0:
                heapq.heappush(heap, count)
        
        queue = collections.deque()
        t = 0
        while heap or queue:
            if queue and queue[0][0] == t:
                    val = queue.popleft()[1]
                    heapq.heappush(heap, val)
            if heap:
                count = heapq.heappop(heap) + 1
                if count < 0:
                    queue.append([t + n + 1, count])
            t += 1
        return t


            

