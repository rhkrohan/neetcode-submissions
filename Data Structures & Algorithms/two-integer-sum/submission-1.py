class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result = []
        i = 0

        for x in nums:
            j = 0
            for y in nums:
                if x + y == target and i != j:
                    result.append(i)
                    result.append(j)
                    return result
                j += 1
            i += 1
        
        return result
        