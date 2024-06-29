class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mymap = set()
        for c in nums:
            if c in mymap:
                return True
            else:
                mymap.add(c)
        return False
