class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count_s = {}
        count_t = {}

        sl = list(s)
        st = list(t)

        for s in sl:
            if s in count_s:
                count_s[s] += 1
            else:
                count_s[s] = 1
        
        for t in st:
            if t in count_t:
                count_t[t] += 1
            else:
                count_t[t] = 1
        
        print(count_s)
        print(count_t)

        return count_s == count_t