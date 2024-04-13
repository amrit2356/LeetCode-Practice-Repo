class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            temp_list = []
            key = ''.join(sorted(word))
            result[key].append(word)
        return list(result.values())
        