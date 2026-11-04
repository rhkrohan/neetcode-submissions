class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDic = {}

        for alphabet in strs:
            tempKey = tuple(sorted(alphabet))

            if tempKey not in anaDic:
                anaDic[tempKey] = [alphabet]
            else:
                anaDic[tempKey].append(alphabet)

        return list(anaDic.values())
