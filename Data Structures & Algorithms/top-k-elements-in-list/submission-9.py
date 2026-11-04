class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = {}
        for i, num in enumerate(nums):
            if num in f:
                f[num] += 1
            else:
                f[num] = 0

            #print(f.items())

        frequencyNum = list(f.items())

        frequencyNum.sort(key = lambda pair : pair[1], reverse=True)

        result = []

        for i in range(k):
            result.append(frequencyNum[i][0])


        return result


        
