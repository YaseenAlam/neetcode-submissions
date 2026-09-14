class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        map1 = {}
        for c in s:
            map[c] = map.get(c, 0) + 1
        for c in t:
            map1[c] = map1.get(c, 0) + 1

        if map1 == map:
            return True
        else:
            return False
