class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Approach:

        1) remove spaces or other noise from our string 
        //lowercase //remove all spaces using replace

        2) two pointers one from the front and one from the back 

        2.5) the length of string should be divisible by 2 or len(str) % 2 == 0

        3) for all points front is equal to back

        4) if front + back == 0 then return true 
        5) else return false

        123 321
        
        
        """
        cleaned_str = "".join(char for char in s.replace(" ", "").lower() if char.isalnum())
        print(cleaned_str)
        print(len(cleaned_str))

        if cleaned_str == "":
            return True
            
        front_index = 0
        back_index = -1
        i = 0

        while i <= len(cleaned_str)/2:

            print(cleaned_str[front_index])
            print(cleaned_str[back_index])

            if (cleaned_str[front_index] != cleaned_str[back_index]):
                return False
            else:
                front_index += 1
                back_index -= 1
            i += 1
        
        return True




        