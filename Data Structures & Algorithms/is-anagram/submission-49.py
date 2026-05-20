class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = {}
        t_dic = {}
        for s_char in s:
            if s_char in s_dic:
                s_dic[s_char] += 1
            else:
                s_dic[s_char] = 0
        
        for t_char in t:
            if t_char in t_dic:
                t_dic[t_char] +=1 
            else:
                t_dic[t_char] = 0

        if s_dic == t_dic:
            return True 

        return False
