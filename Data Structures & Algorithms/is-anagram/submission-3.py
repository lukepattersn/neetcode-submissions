class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            # Increment character count, defaulting to 0 if not in dictionary.
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Check to see if the HashMap's are not anagrams of eachother
        for c in countS:# Iterating through all key values of countS
            if countS[c] != countT.get(c,0): # If the key doesn't exist have the default value for key error
                return False

        return True # Are Anagrams