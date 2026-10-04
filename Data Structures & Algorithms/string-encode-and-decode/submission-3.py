class Solution:
    """
    we know the characters are limited from 0 to 256 

    """

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            for char in string:
                res = res + str(ord(char)) + "."
            res = res + "new."
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        decoded = s.split(".")
        res = []
        temp_str = ""
        for token in decoded:
            if token != "new" and token != "":
                temp_str += (chr(int(token)))
            else:
                res.append(temp_str)
                temp_str = ""
        return res[:-1]
        # return s.split("\\space/") if s is not "" else []
