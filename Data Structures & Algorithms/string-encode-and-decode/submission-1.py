class Solution:

    def encode(self, strs: List[str]) -> str:
        
        lengthWord = len(strs)
        result = "" #+ str(lengthWord)

        for word in strs:
            for alpha in word:
                result += alpha

            result += "----------"
        
        print(result)

        return result
            

    def decode(self, s: str) -> List[str]:
        result = s.split("----------")

        result.pop()

        print(result)


        return result
