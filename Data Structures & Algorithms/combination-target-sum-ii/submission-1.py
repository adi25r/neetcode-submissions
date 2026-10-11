class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # given candidates w dups
        # given target
        # want unique combos where chosen numbers sum to target

        candidates.sort()
        res = []

        curr_list = []
        def backtrack(i, curr_total):
            if curr_total == target:
                res.append(curr_list.copy())
                return
            if i >= len(candidates) or curr_total > target:
                return
            
            # choose this number
            curr_list.append(candidates[i])
            j = i + 1
            backtrack(j, curr_total + candidates[i])
            curr_list.pop()

            # don't
            while j in range(len(candidates)) and candidates[j] == candidates[i]:
                j += 1
            backtrack(j, curr_total)

        backtrack(0, 0)
        # for i in range(len(res)):
        #     res[i] = tuple(res[i])
        
        # tmp = list(set(res))

        # for i in range(len(tmp)):
        #     tmp[i] = list(tmp[i])

        return res

        