from typing import List

# two pointer approach worst case O(n log n) IF they have asked for the numbers rather than the indices
# if they ask for indices this does not work and you cant make it work since duplicates case breaks the hash lookup and
# you cant add as you emliminate elements which dont work by moving pointers as array is sorted so you have lost original indices.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      # insert all elements into dict (hash table)
        nums = sorted(nums) # merge sort array
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] < target: # smaller than target increase i as this num does not work with any other number (think about why)
                i = i + 1
            elif nums[i] + nums[j] > target: # bigger than target increase j as this num does not work with any other number
                j = j - 1
            else:
                return [nums[i],nums[j]] 
        return []
