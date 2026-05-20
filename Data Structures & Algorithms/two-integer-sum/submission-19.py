class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
    two pointers

    initialArr = -
    > given

    i -> from the left side 
    j -> from the right side 

    i < j or maybe equal too

    algorithm 

    [3, 4, 5, 6]

    i = 0
    j = len(nums) - 1 -> last item 

    while i <= j:
        if initial[i] + initial[j] == k:
            return [i, j]
        i += 1
        j -= 1
    
    
    """


    # nums -> int list        target-> int

        j = len(nums) - 1 

        for i in range(0,len(nums)):
            j = len(nums) - 1
            print(f"{i} Index started")
            print(f"INITIAL VALUES: i = {i} j = {j}")
            
            while i < j:
                print(f" Testing j = {j}")
                if nums[i] + nums[j] == target and i != j:
                    print(f"Found: i {i}, j {j}") # [3, 4, 5, 6] target = 7
                    return [int(i), int(j)]
                j -= 1  
                #print(f"Jth index: {j}")
                

            

        