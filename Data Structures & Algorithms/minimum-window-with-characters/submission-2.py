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

        """
        better solution: 
        Slide a window across, using left and right pointers
        move right until we match, then slide left until we don't anymore
        record minimum string somewhere

        do a frequency analysis of t
        keep track of a counter as well, just to make it simple to keep track as we slide window

        slide r
        """
        res = ""

        t_freq = {}
        for i in range(len(t)):
            t_freq[t[i]] = 1 + t_freq.get(t[i], 0)

        have, need = 0, len(t)
        l = 0
        window_freq = {}
        for r in range(len(s)):
            char = s[r]
            window_freq[char] = 1 + window_freq.get(char, 0)

            if char in t_freq:
                if window_freq[char] <= t_freq[char]:
                    have += 1
            
            while have == need:
                if r - l + 1 < len(res) or res == "":
                    res = s[l:r + 1]
                window_freq[s[l]] -= 1
                if s[l] in t_freq and window_freq[s[l]] < t_freq[s[l]]:
                    have -= 1
                l += 1
        
        return res



        # t_freq = {}
        # for i in range(len(t)):
        #     t_freq[t[i]] = 1 + t_freq.get(t[i], 0)

        # for w_len in range(len(t), len(s) + 1):
        #     for s_pos in range(len(s) - w_len + 1):
        #         test_freq = {}
        #         for i in range(w_len):
        #             # print(str(s_pos) + " " + str(i) + " " + str(w_len))
        #             test_freq[s[s_pos + i]] = 1 + test_freq.get(s[s_pos + i], 0)
                
        #         contains = True
        #         for key, value in t_freq.items():
        #             if not key in test_freq or not test_freq[key] >= value:
        #                 contains = False
        #                 break
                    
        #         if contains:
        #             return s[s_pos:s_pos + i + 1]


        # return ""