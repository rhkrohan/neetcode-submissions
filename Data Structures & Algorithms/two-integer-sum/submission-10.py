class Solution:
    """
    Approach

    - int target --- arr[int] nums 
    - may use sliding window
    - target - num[index] = arr[int] -> options 
    - two pointers, i, j
    
    Algorithm 
    - subtract all elements from 7 and hash the results


    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dic = {}

        for i, x in enumerate(nums):

            complement = target - x

            if complement in nums_dic:
                return list([nums_dic[complement], i])

            nums_dic[x] = i

            




        
 
            
            