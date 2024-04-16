class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = []
  
        def backtrack(start):

            if start == len(nums):
                if nums not in permutations:
                    permutations.append(nums[:])
            
            else:
                for i in range(start, len(nums)):
                    nums[start], nums[i] = nums[i], nums[start]
                    backtrack(start + 1)
                    nums[start], nums[i] = nums[i], nums[start]


        backtrack(0)
        return permutations