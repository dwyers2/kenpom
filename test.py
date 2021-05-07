class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = int()
        endIndex = len(s)
        
        for index, curNum in enumerate(s):
            if(curNum == "I" ):                
                if(index < endIndex and s[index+1] in ("V","X")):
                    total -= 1
                else:
                    total += 1
            if(curNum == "V"):
                total += 5
            elif(curNum == "X"):
                if( index < endIndex and s[index+1] in ("L","C") ):
                    total -= 10
                else:
                    total += 10
            elif(curNum == "C" ):
                if( index < endIndex and s[index+1] in ("D", "M")):
                    total -= 100
                else:
                    total += 100
            elif(curNum == "L"):
                total += 50
            elif(curNum == "C"):
                total += 100
            elif(curNum == "D"):
                total += 500
            elif(curNum == 'M'):
                total += 1000
                    
        return total
        
s = Solution()        
print(s.romanToInt("IV"))