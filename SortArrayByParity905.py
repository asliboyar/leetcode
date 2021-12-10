class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        first = 0
        last = len(nums)-1
        while first < last:
            if nums[first]%2==0:
                first +=1
            else:
                a = nums[first]
                nums [first] = nums[last]
                nums[last] = a         
                last-=1
        return nums
