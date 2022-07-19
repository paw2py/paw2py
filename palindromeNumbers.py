palenddrom numnbers 121
class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstr = str(x)
        print(xstr[::-1])
        for i in range(len(xstr)):
            print(xstr[len(xstr) -i-1])
            if xstr[i] != xstr[len(xstr) -i-1]:
                return False
          
        return True
        

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return False if x < 0 else x == int(str(x)[::-1])      
