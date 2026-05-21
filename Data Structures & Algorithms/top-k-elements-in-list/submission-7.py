from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        """
        integer arr -> nums
        integer -> k
        k most frequent elements -> return 
        
        """


        """
        store the numbers in a hashmap with frequency count an
        number as the key 



        number_map = 

        for num in nums:


        """ "O(n)"


        number_map = defaultdict(int) 

        for num in nums: 
            number_map[num] += 1

        """
        [1, 2, 2, 2, 3, 3, 3]
        3 : 3
        2 : 2
        1 : 1

        """

        result = list(sorted(number_map.items(), key=lambda x : x[1], reverse=True))

        print(result)

        result_list = []

        for i in range(k):
            result_list.append(result[i][0])

        return result_list
            




            