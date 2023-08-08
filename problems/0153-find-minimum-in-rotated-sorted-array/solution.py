class Solution:
    def findMin(self, nums: List[int]) -> int:
        def recfm(numsl):
            k = len(numsl) // 2
            if len(numsl) == 2:
                return min(numsl)
            elif len(numsl) == 1:
                return numsl[0]
            elif numsl[len(numsl) - 1] < numsl[k]:
                return recfm(numsl[k:len(numsl)])
            elif (numsl[0] > numsl[k]):
                return recfm(numsl[0:k+1])
            else:
                return recfm(numsl[0:k+1])
        return recfm(nums)
