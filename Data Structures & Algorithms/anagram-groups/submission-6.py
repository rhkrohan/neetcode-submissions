class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDic = {}

        for alphabet in strs:
            tempKeyDic = {}
            for alpha in alphabet:
                if alpha not in tempKeyDic:
                    tempKeyDic[alpha] = 1
                else:
                    tempKeyDic[alpha] += 1

            #print(tempKeyDic)
            tempKeyTuple = tuple(sorted(tempKeyDic.items()))
            #print(tempKeyTuple)

            

            if tempKeyTuple not in anaDic:
                anaDic[tempKeyTuple] = [alphabet]
            else:
                anaDic[tempKeyTuple].append(alphabet)

        resultList = list(anaDic.values())

        #print(resultList)

        return resultList




        