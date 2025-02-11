class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        for i in range(len(nums)):
            target = - (nums[i])
            start = i+1
            end = len(nums) - 1
            while start < end:
                print(nums)
                print(f"target = {target}")
                print(f"start = {nums[start]}")
                print(f"end = {nums[end]}")
                if nums[start] + nums[end] < target:
                    start = start + 1
                elif nums[end] + nums[start] > target:
                    end = end - 1
                elif nums[end] + nums[start] == target:
                    result.add((nums[i], nums[start], nums[end]))
                    start = start + 1
                    end = end - 1
                    print("found")      
        return [list(i) for i in result]
