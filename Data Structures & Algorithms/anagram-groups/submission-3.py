from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        strategy

        sort each string and use as signature for storing anagrams for that word


        key = ''.join.sorted(word)

        and then make a wordmap of signature as the key and the array of anagrams as the value

        """


        word_map = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            word_map[key].append(word)



        return list(word_map.values())

