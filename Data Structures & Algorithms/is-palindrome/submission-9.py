class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.strip()
        l = 0
        r = len(s)-1
        while l < r:
            left = s[l]
            if not left.isalnum():
                l+=1
                continue
            right = s[r]
            if not right.isalnum():
                r-=1
                continue
            left = left.lower()
            right = right.lower()
            if right != left:
                return False
            l+=1
            r-=1
        return True
            
        