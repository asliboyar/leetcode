class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newnums = nums.copy()
        for i in range(len(nums)):
            newnums.remove(nums[i])
            a = target-nums[i]
            if a in newnums:
                nums[i] = None
                return [nums.index(None),nums.index(a)]
