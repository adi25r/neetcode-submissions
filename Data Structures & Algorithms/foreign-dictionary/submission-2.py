class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # the first differing letter between any 2 strings 
        # enforces a dependency
        # n -> f
        # h -> e 
        # r -> n
        # e -> r
        # h e r n f
        n = len(words)
        adj_list = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for k in range(min_len):
                if w1[k] != w2[k]:
                    adj_list[w1[k]].add(w2[k])
                    break
        
        # now that we have a graph, we just need a topological ordering
        res = []
        visiting = {}
        def dfs(n):
            if n in visiting:
                return visiting[n]
            
            visiting[n] = True
            
            for neigh in adj_list[n]:
                if dfs(neigh):
                    return True

            visiting[n] = False
            res.append(n)
            return False
            
        
        for c in adj_list:
            if c not in visiting:
                if dfs(c):
                    return ""
        
        return "".join(res[::-1])
 
                

