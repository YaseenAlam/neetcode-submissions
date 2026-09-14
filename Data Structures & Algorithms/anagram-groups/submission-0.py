class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1 = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in map1:
                map1[key] = []
            map1[key].append(s)

        return list(map1.values())