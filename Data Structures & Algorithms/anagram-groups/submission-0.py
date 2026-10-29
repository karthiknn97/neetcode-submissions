class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i, word in enumerate(strs):
            countChar = [0] * 26
            for ch in word:
                countChar[ord(ch) - ord('a')] += 1
            key = tuple(countChar)
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
        return list(anagrams.values())
                