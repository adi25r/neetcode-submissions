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
        visiting = set()
        visited = set()

        # if c is in visiting, we must be in a cycle --> false
        def dfs(c):
            if c in visited:
                return True
            if c in visiting:
                return False
            
            visiting.add(c)

            for neigh in adj_list[c]:
                if not dfs(neigh):
                    return False
            
            visiting.remove(c)
            res.append(c)
            visited.add(c)
            return True
        
        for char in adj_list:
            if char not in visiting:
                if not dfs(char):
                    return ""
        
        return "".join(res[::-1])
 
                

