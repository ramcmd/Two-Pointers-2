# TC: O(n)
# SC: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        pointer = 1
        counter = 1
        
        i = 1
        
        while pointer < len(nums):
            # set the pointer
            if nums[pointer] == nums[pointer-1]:
                counter += 1
            else:
                counter = 1
                
            if counter <= 2: 
                nums[i] = nums[pointer]
                i += 1
            
            pointer += 1
            
        return i
            
            
            
            
            
                
                
            