class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            countChar = [0] * 26
            for ch in word:
                countChar[ord(ch) - 97] += 1
            key = tuple(countChar)
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
        return list(anagrams.values())
                