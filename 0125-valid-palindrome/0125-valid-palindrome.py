class Solution:
    def isPalindrome(self, s: str) -> bool:
        res="".join(filter(str.isalnum,s))
        res=res.lower()
        if res==res[::-1]:
            return True
        else:
            return False