class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        for num in nums:
            duplicate[num] = 0
        for num in nums:
            if duplicate.get(num) == 1:
                return True
            duplicate[num] = 1
        return False
         