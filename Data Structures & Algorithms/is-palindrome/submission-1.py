import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for char in s:
            if char in string.ascii_letters or char in string.digits: 
                res += char.lower()
        return res == res[::-1]
            