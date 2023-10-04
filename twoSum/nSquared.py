from typing import List

# brute force approach O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(len(nums)):
            for k in range(len(nums)):
                if (n!=k):
                    if (nums[n] + nums[k] == target):
                        return  [n,k]
        return []
