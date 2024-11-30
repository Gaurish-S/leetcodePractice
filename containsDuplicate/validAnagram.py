class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        for i,j in zip(s,t):
            dict_s[i] = 0
            dict_t[j] = 0
        for i,j in zip(s,t):
            dict_s[i] += 0
            dict_t[j] += 0
        
        return dict_s == dict_t
