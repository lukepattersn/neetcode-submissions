class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}

        for str in strs:
            joined_str = "".join(sorted(str))
            if joined_str in anagramMap:
                anagramMap[joined_str] += [str]
                continue
            
            anagramMap[joined_str] = [str]
        return list(anagramMap.values())
