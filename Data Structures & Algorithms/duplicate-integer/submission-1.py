class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 1
        for element in nums:
            x = element 
            for match_element in nums[i:]:
                y = match_element
                if y == x:
                    return True
            i += 1
        return False
         