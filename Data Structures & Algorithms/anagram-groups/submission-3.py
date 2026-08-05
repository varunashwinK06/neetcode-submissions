class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_array=defaultdict(list)
        for word in strs:
            count=[0] * 26
            for c in word:
                count[ord(c)-ord('a')]+=1
            char_array[tuple(count)].append(word)
        return list(char_array.values())


        