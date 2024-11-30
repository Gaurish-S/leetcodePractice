class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # insert all elements into dict (hash table)
        numsDict = {}
        for i in range(len(nums)):
            numsDict[str(nums[i])] =  []
        for i in range(len(nums)):
            numsDict[str(nums[i])].append(i)

        for i in range(len(nums)):
            try:
                idx_list = numsDict[str(target - nums[i])] # look for difference (hash lookup)
                if len(idx_list) > 1: # make sure same index is not returned
                    if idx_list[0] == i:
                        return sorted([i,idx_list[1]])
                    else:
                        return sorted([i, idx_list[0]])
                if len(idx_list) == 1 and idx_list[0] != i:
                    return sorted([i, idx_list[0]])
            except KeyError: # in case no working idx exists for current num[i]
                continue
        return []        
        
