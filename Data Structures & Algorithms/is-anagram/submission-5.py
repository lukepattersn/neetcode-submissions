class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        res, res2 = Counter(s), Counter(t)
        return res == res2