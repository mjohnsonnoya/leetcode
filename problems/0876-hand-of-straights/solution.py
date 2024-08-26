class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = {}
        for card in hand:
            if card not in count:
                count[card] = 1
            else:
                count[card] += 1
        
        print(count)
        heap = (list(count.keys()))

        heapq.heapify(heap)

        while heap:
            minval = heap[0]
            for i in range(minval, minval + groupSize):
                if i not in count or count[i] <= 0:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != heap[0]:
                        return False
                    else:
                        heapq.heappop(heap)
        
        return True
                

