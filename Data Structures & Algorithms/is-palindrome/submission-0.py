class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = "".join([char for char in s if char.isalnum()])
        print(s2)
        l = 0
        r = len(s2) - 1

        while l < r:
            if s2[l].lower() != s2[r].lower():
                return False
            l += 1
            r -= 1
        return True
        