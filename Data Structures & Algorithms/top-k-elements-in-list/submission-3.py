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

        result_frequency = []
        k_maximum_frequencies = list(number_map.values())
        for i in range(1, k+1): 
            maximum = max(k_maximum_frequencies)
            result_frequency.append(maximum)
            k_maximum_frequencies.remove(maximum)
            #print(maximum)

        result = []
        for key in number_map: 
            print(key)
            print(result_frequency)
            print(number_map[key])
            if number_map[key] in result_frequency:
                result.append(key)

        return result
            




            