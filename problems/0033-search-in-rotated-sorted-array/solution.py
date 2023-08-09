# class Solution:
#     def binsearch(self,numslist, target) -> int:
#             k = len(numslist)//2
#             if len(numslist) == 1:
#                 if numslist[0] == target:
#                     return 0
#                 else:
#                     return -1
#             elif target >= numslist[k]:
#                 return k + self.binsearch(numslist[k:],target)
#             else:
#                 return self.binsearch(numslist[0:k],target)
#     def search(self, nums: List[int], target: int) -> int:
#         def recsearch(numslist: List[int]):
#             k = len(numslist)//2
#             if numslist[0] <= target < k:
#                 return self.binsearch(numslist[0:k],target)
#             elif numslist[k] <= target <= numslist[-1]:
#                 return k + self.binsearch(numslist[k:],target)
#             elif numslist[0] > numslist[k] and target <= numslist[0]:
#                 return recsearch(numslist[0:k])
#             elif numslist[k] >= numslist[-1] and target <= numslist[-1]:
#                 return k + recsearch(numslist[k:])
#             elif numslist[0] >= target <= numslist[k]:
#                 return recsearch(numslist[0:k+1])
#             elif numslist[k] >= target <= numslist[-1]:
#                 return k + recsearch(numslist[k:])
#             else:
#                 return -1
            
#         return recsearch(nums)

from typing import List

class Solution:
    def binsearch(self, nums: List[int], target: int, left: int, right: int) -> int:
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid

            # If left side is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    return self.binsearch(nums, target, left, mid)
                left = mid + 1
            # If right side is sorted
            else:
                if nums[mid] <= target <= nums[right]:
                    return self.binsearch(nums, target, mid, right)
                right = mid - 1

        return -1


            
            



