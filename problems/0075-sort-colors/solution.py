class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def merge(nums1, nums2):
            l = 0
            r = 0
            res = []
            while l < len(nums1) or r < len(nums2):
                if l == len(nums1):
                    res += nums2[r:]
                    break
                elif r == len(nums2):
                    res += nums1[l:]
                    break
                else:
                    if nums1[l] <= nums2[r]:
                        res.append(nums1[l])
                        l += 1
                    else:
                        res.append(nums2[r])
                        r += 1
            return res       

        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
            k = len(nums) // 2
            return merge(mergeSort(nums[:k]), mergeSort(nums[k:]))


        nums[:] = mergeSort(nums)
