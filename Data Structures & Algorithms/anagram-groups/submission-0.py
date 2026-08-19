class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        l = []

        for i in strs:
            s = tuple(sorted(i))
            if s not in d:
                d[s] = []

            d[s].append(i)

        for j in d.values():
            l.append(j)

        return l

