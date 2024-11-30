def hasDuplicate(self, nums: List[int]) -> bool:
    dict = {}
    for i in nums:
        dict[str(i)] = 0
    for i in nums:
        dict[str(i)] += 1
        if dict[str(i)] == 2:
            return True

    return False
            

