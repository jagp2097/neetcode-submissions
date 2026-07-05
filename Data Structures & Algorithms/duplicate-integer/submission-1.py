class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        while len(nums) > 1:
            number = nums.pop(0)

            if number in nums:
                return True

        return False        
            
        