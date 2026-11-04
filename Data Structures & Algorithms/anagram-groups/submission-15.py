class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # making a frequency array of 26 zeros a 26 zeross matrix where you update each index by using a clever strategy

        # ord(alphabet) - ord(a)
        """
        ord(a) -> 97.  - ord(a). -> 0th index
        ord(b) -> 98.  - ord(a)  -> 1st index
        ord(c) -> 99
        ord(d) -> 100.  
        ord(z) -> 122 - ord(a) -> 25th index
         
        """

        
        anaDic = {}
        #making the 26 zeros ist
  

        for alphabet in strs:
            # making the unique zero matrix
            count = [0] * 28

            for eachAlpha in alphabet:
                     
                # finding and updating index using the unique startegy
                index = ord(eachAlpha) - ord('a')
                #print(f"{eachAlpha}: {index}")
                count[index] += 1

            tempKey = tuple(count)

            #print(f"{alphabet}: {tempKey}")

            if tempKey not in anaDic:
                anaDic[tempKey] = [alphabet]
            else:
                anaDic[tempKey].append(alphabet)

        return list(anaDic.values())
