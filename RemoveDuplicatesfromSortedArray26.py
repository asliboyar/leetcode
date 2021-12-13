class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == nums[i-1]:
                nums[i-1] = nums[i]
                count+=1
        return count
