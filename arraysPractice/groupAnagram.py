class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angm_dict = {}
        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted in angm_dict:
                angm_dict[s_sorted].append(s)
            else:
                angm_dict[s_sorted] = [s]
        return angm_dict.values()
