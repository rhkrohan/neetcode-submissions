class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numDic = {}

        for i, num in enumerate(nums):
            numDic[num] = i

        for i, num in enumerate(nums):
            complement = target - num

            if complement in numDic and i != numDic[complement]:
                return [i, numDic[complement]]

        return [0, 0]