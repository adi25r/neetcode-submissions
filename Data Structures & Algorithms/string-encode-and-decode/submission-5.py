class Solution:
    """
    we know the characters are limited from 0 to 256 

    """

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            for char in string:
                res.append(str(ord(char)) + ".")
            res.append("new.")
        print(res)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        decoded = s.split(".")
        res = []
        temp_str = []
        for token in decoded:
            if token != "new" and token != "":
                temp_str.append((chr(int(token))))
            else:
                res.append("".join(temp_str))
                temp_str = []
        return res[:-1]
        # return s.split("\\space/") if s is not "" else []
