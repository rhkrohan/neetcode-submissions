class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        
        strategy:

        sliding window problem ->  one 

        we go from from left to right

        we keep a check for the lowest price seen so far
        

        and when we move to a new element 

        if new element is less than the least seeen so far we update our least seen so far

        else:

            then we compute new max profit if least - new < max_profit 

         "[10, 1, 5, 6, 7, 1]" -> buying it at 1 and we see when value is 7 so our profit is 6

        
        
        """

        # if prices list is null return 0


        # track minimum value so far 

        minSoFar = prices[0] 
        bestProfit = 0

        # sliding window
        for p in prices[1:]:
            if p < minSoFar:
                minSoFar = p
            else:
                candBestProfit = p - minSoFar
                if candBestProfit > bestProfit:
                    bestProfit = candBestProfit

        return bestProfit



        

        

        


        

        