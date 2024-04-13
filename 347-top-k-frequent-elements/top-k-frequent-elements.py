from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {} 
        if k == len(nums):
            return nums

        for i in set(nums):
            countMap[i] = nums.count(i)
        
        return heapq.nlargest(k, countMap.keys(), key=countMap.get)