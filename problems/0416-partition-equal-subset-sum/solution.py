
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = set()
        target = sum(nums) / 2
        print(target)
        if not target - int(target):
            target = int(target)
            for num in nums:
                if num == target:
                    return True
                temp_sums = set()
                for i in sums:
                    if num + i == target:
                        return True
                    elif num + i < target:
                        temp_sums.add(num + i)
                sums.update(temp_sums)
                sums.add(num)
        else:
            return False
