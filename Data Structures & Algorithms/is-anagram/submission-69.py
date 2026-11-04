class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sDic = {}
        tDic = {}

        for alpha in s:
            if alpha not in sDic:
                sDic[alpha] = 1
            else:
                sDic[alpha] += 1
        
        for beta in t:
            if beta not in tDic:
                tDic[beta] = 1
            else:
                tDic[beta] += 1

        print(sDic, tDic)
        if sDic == tDic:
            return True
        
        return False
        