class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
             s = s + word + ";"
        return s

    def decode(self, s: str) -> List[str]:
        temp = ""
        res = []
        for a in s:
            if a == ";":
                res.append(temp)
                temp = ""
            else:
                temp = temp + a
        return res