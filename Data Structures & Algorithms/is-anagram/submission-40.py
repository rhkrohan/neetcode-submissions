class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)

        if len(s_list) != len(t_list):
            return False

        s_new_list = s_list[:]
        t_new_list =  t_list[:]

        for s in s_list:
            if s in t_new_list:
                t_new_list.remove(s)
            else:
                return False
            
        if t_new_list == []:
            return True

        return not t_list_new     
        
           