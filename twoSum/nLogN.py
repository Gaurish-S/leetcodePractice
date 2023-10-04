from typing import List

# merge sort with n binary searches approach O(n log n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted(nums) # merge sort ideally
        for i in range(len(nums)):
            idx = -1
            try:
               idx = nums.index((target - nums[i])) # look for difference (binary search ideally)
               if idx == i: # make sure same index is not returned
                   continue
               return [i, idx]
            except ValueError: # in case no working idx exists for current num[i]
                continue
        return []
