class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = {}
        t_dic = {}

        if len(s) != len(t):
            return False

        for alpha, beta in zip(s, t):
            s_dic[alpha] = s_dic.get(alpha, 0) + 1
            t_dic[beta] =  t_dic.get(beta, 0) + 1
        
        if s_dic == t_dic:
            return True
        
        return False