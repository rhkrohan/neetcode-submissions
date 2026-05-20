class Solution:
    """
    
    Approach:

    check if element - target == elements from dictionary 
    if true:
        indicies in array
    else:
        Add element to dictionary, key = element, value = index
        return false
    
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dic = {}
        index = 0
        for element in nums:
            complement = target - element
            if complement in nums_dic.keys():
                return [nums_dic[complement], index]
            else:
                nums_dic[element] = index
                index += 1
        print(nums_dic)
        return [1, 2]
        