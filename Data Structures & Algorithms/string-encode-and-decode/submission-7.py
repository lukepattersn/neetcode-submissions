class Solution:
    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(s)}#{s}' for s in strs)
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = s.find('#', i)  # Find the index delimiter starting from index i
            length = int(s[i:j])  # Extract the length of the word & convert it to an integer
            i = j + 1  # Move to the first char of the  word
            res.append(s[i:i+length])  # Extract the word of length characters & append to list
            i += length  # Move i to the start of the next word
        return res