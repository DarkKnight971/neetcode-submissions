class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in nums:
                b = nums.index(complement)

                if b != i:
                    return sorted([b, i])
                
