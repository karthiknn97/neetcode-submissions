class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict();
        if len(s) != len(t):
            return False
        for sc, tc in zip(s,t):
            d[sc] = d.get(sc,0) + 1
            d[tc] = d.get(tc,0) - 1
        return all(v==0 for v in d.values())