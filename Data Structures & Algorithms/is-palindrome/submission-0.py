class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for c in s:
            if not c.isalnum():
                continue
            else:
                res += c.lower()
        revers = res[::-1]
        if revers == res:
            return True
        print(res)
        print(revers)
        return False