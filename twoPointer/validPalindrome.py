class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        second = len(s) - 1
        s = s.lower()
        while first <= second:
            if not s[first].isalnum():
                first += 1
                continue
            if not s[second].isalpha():
                second -= 1
                continue          
            if s[first] != s[second]:
                return False
            
            first += 1
            second -= 1
        return True
