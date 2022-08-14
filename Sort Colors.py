#TC: O(n) with the 3 pointer approach
#SC: O(1) in place algorithm

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        high = len(nums) -1
        mid = 0
        
        while (mid <= high):
            if nums[mid] == 1:
                mid+= 1
            elif nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high-=1
        