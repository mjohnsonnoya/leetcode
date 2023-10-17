class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
#         cache = {}
        
#         def helper(i, j, p):
            
#             if (i, j, p) in cache:
#                 return cache[(i, j, p)]
#             if i > j:
#                 return 0
#             if i == j:
#                 cache[(i, j, p)] = piles[i] if p else -piles[i]
#                 return cache[(i, j, p)]
#             if p:
#                 cache[(i, j, p)] = max(helper(i + 1, j, not p) + piles[i], helper(i, j - 1, not p) + piles[j])
#             if not p:
#                 cache[(i, j, p)] = min(helper(i + 1, j, not p) - piles[i], helper(i, j - 1, not p) - piles[j])
#             return cache[(i, j, p)]
#         return helper(0, len(piles) - 1, True) > 0
