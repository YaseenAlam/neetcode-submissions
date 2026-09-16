class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for strin in strs:
            final = final + f"{len(strin)}#{strin}"
        return final

    def decode(self, s: str) -> List[str]:
        final = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            start_of_str = j + 1
            end_of_str = start_of_str + length

            final.append(s[start_of_str:end_of_str])

            i = end_of_str
        return final



