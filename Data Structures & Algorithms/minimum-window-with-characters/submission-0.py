class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        naive sol'n.

        iterate from size of t to size of s (window length)
        use freq map of t
        for every window length location, see if window matches perm length
        return string on first occurence
        otherwise nothing
        """
        t_freq = {}
        for i in range(len(t)):
            t_freq[t[i]] = 1 + t_freq.get(t[i], 0)

        for w_len in range(len(t), len(s) + 1):
            for s_pos in range(len(s) - w_len + 1):
                test_freq = {}
                for i in range(w_len):
                    # print(str(s_pos) + " " + str(i) + " " + str(w_len))
                    test_freq[s[s_pos + i]] = 1 + test_freq.get(s[s_pos + i], 0)
                
                contains = True
                for key, value in t_freq.items():
                    if not key in test_freq or not test_freq[key] >= value:
                        contains = False
                        break
                    
                if contains:
                    return s[s_pos:s_pos + i + 1]


        return ""