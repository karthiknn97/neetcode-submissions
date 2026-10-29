class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict();
        if len(s) != len(t):
            return False
        for sc, tc in zip(s,t):
            if sc in d:
                d[sc] += 1
            else:
                d[sc] = 1
            if tc in d:
                d[tc] -= 1
            else:
                d[tc] = -1
        return all(v==0 for v in d.values())