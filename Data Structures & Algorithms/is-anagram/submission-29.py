class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Convert both strings to lists of characters
        s_list = list(s)
        t_list = list(t)
        
        # Check if lengths are equal; if not, they cannot be anagrams
        if len(s_list) != len(t_list):
            return False
        
        # Copy lists to avoid modifying the original lists
        s_new_list = s_list[:]
        t_new_list = t_list[:]
        
        # Remove matching characters from t_new_list
        for alphabet_s in s_list:
            if alphabet_s in t_new_list:
                t_new_list.remove(alphabet_s)
            else:
                # If any character in `s` isn't found in `t`, they are not anagrams
                return False
        
        # If t_new_list is empty after removing all matches, they are anagrams
        return not t_new_list
