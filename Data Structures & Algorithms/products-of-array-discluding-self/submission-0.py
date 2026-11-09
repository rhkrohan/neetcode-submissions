class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product = 1
        zeroPresent = False
        zero = []

        for i, num in enumerate(nums):
            if num == 0:
                zero.append(i)
                zeroPresent = True
                product *= 1
            else:
                product *= num

        print(product)

        result = []

        for i, num in enumerate(nums):
            if zeroPresent == True:
                if num == 0 and len(zero) >= 2:
                    result.append(0)
                elif num == 0 and len(zero) == 1:
                    result.append(product)
                elif num != 0 and len(zero) >= 1:
                    result.append(0)
                else:
                    print('never executes')
            else:            
                current = product / num
                result.append(int(current))

        
        return result


        