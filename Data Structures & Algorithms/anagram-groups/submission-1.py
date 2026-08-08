
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}
        for s in range(len(strs)):
            key = "".join(sorted(strs[s]))
            if key in anagramMap:
                anagramMap[key].append(strs[s])
            else:
                anagramMap[key] = [strs[s]]
        return list(anagramMap.values())