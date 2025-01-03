class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # put nums in buckets which represent diff frequencies
        nums.sort() # if you dont want to sort can use dict instead as has "O(1)" access
        buckets = [[] for _ in range(len(nums)+1)] # max freq n, min freq 0 so need n+1 buckets
        numFreq = 0
        for i in range(len(nums)):
            if (i != 0 and nums[i] != nums[i-1]):
                buckets[numFreq].append(nums[i-1])
                numFreq = 0
            numFreq += 1
        # last num remains to be added
        buckets[numFreq].append(nums[-1])
        print(buckets)

        # get top k
        numCount = 0
        topK = []
        for b in reversed(buckets):
            for i in b:
                if numCount == k:
                    break
                topK.append(i)
                numCount += 1

            if numCount == k:
                break
        return topK


