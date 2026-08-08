class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}
        for str in strs:
            group = tuple(sorted(str))
            if group not in anagramMap:
                anagramMap[group] = [str]
            else:
                anagramMap[group].append(str)
        return list(anagramMap.values())
        