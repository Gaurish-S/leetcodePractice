class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            code += "#" + str(len(s)) + s
        return code
        
    def decode(self, s: str) -> List[str]:
        res = []
        for i in range(len(s))
            if s[i] == "#":
                res.append(s[i+2:i+int(s[i+1])+1])
            i += int(i+ int(s[i+1]))
        return res
