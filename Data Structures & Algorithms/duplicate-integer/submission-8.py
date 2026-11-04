class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dicNum = {}

        for i, num in enumerate(nums):
            if num in dicNum:
                return True
            dicNum[num] = i
        
        return False
         
        