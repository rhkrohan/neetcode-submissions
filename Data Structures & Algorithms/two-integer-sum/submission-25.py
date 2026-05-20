class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        store all nums with indexes in a dictionary
        
        numsDic = {}

        numsDic[ithNum] = index -> O(n)


        go through list once and try to find the complement 

        i = 0

        complement = target - nums[i]

        if complement in numsDic:
            return [i, numsDic[complement]]

        """


        # nums -> int list        target-> int

        numsDic = {}
        ithIndex = 0

        for num in nums:   # -> O(n)
            numsDic[num] = ithIndex
            ithIndex += 1

        i = 0
        for num in nums:
            #print(i)
            complement = target - num
            if complement in numsDic.keys() and i != numsDic[complement]:
                return [i, numsDic[complement]]
            i += 1
            
        


        

            

        