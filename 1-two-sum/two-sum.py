class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rtype = []
        numHashmap = {}
        for index, number in enumerate(nums):
            complement = target - number
            if complement in numHashmap:
                rtype = [numHashmap[complement], index]

            numHashmap[number] = index

        return rtype