class Solution:
    def encode(self, strs: List[str]) -> str:
        res = "" #create empty string
        for s in strs:
            res += str(len(s)) + "#" + s # append onto str: strlen, '#' and s
        return res
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1 # wait to hit a delimiter
            length = int(s[i:j])
            i = j + 1 # move onto next word
            j = i + length
            res.append(s[i:j])
            i = j # set i to be on the start of the next word

        return res