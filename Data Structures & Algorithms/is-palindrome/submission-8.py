class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            while l < r and not s[l].isalnum():
                l += 1
                print(l, s[l])
            while r > l and not s[r].isalnum():
                r -= 1
                print(r, s[r])
            if s[r].lower() != s[l].lower():
                print(s[r].lower(), s[l].lower())
                return False
            print(l, s[l])
            print(r, s[r])
            print("#-----")
            l += 1
            r -= 1
        return True
