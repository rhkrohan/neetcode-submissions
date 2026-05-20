from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)  # key: signature, value: list of words
        
        for word in strs:
            # signature: sorted letters as a string
            signature = ''.join(sorted(word))
            groups[signature].append(word)
        
        return list(groups.values())
