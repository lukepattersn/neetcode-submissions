class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # count occurances of each char
        res = 0 # longest substring we can create w/ k replacements

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k: # of replacements we have to do
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res
