class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for word in strs:
            sort = ''.join(sorted(word))
            if sort in hashMap.keys():
                hashMap[sort].append(word)
            else:
                hashMap[sort] = [word]
        return list(hashMap.values())