class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count = {}

        for x in s:
            count[x] = 0
        for y in t:
            count[y] = 0

        for x in s:
            count[x] += 1

        for y in t:
            count[y] -= 1

        for j in count.values():
            if j != 0:
                return False

        return True