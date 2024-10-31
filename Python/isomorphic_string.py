class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapST = {}  
        mapTS = {}  

        for sChar, tChar in zip(s, t):
            if sChar in mapST:
                if mapST[sChar] != tChar:
                    return False
            else:
                mapST[sChar] = tChar
            
            if tChar in mapTS:
                if mapTS[tChar] != sChar:
                    return False
            else:
                mapTS[tChar] = sChar

        return True
