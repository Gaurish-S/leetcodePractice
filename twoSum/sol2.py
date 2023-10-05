from typing import List

# dict lookup of difference approach average O(n), worst case still O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # insert all elements into dict (hash table)
        numsDict = {}

        for i in range(len(nums)):
            idx = -1
            try:
               idx = numsDict[str(target - nums[i])] # look for difference (hash lookup)
               if idx == i: # make sure same index is not returned
                   continue
               return [i, idx]
            except KeyError: # in case no working idx exists for current num[i]
                numsDict[str(nums[i])] = i
        return []
