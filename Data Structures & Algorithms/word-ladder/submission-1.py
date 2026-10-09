from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # let's build a graph here. 

        def can_be_neighbor(w1, w2):
            num_diff = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    num_diff += 1
                    if num_diff == 2:
                        return False
            return True
        
        adj_list = defaultdict(list)

        for i in range(len(wordList)):
            for j in range(i, len(wordList)):
                if i == j: continue
                w1, w2 = wordList[i], wordList[j] 
                if can_be_neighbor(w1, w2):
                    adj_list[w1].append(w2)
                    adj_list[w2].append(w1)
            
        for i in range(len(wordList)):
            if can_be_neighbor(beginWord, wordList[i]):
                adj_list[beginWord].append(wordList[i])
                adj_list[wordList[i]].append(beginWord)
    
        # run bfs from beginning, see if we can get to end
        visit = set()
        frontier = deque([beginWord])
        visit.add(beginWord)

        num_hops = 1

        while frontier:
            size = len(frontier)
            for i in range(size):
                curr = frontier.popleft()

                if curr == endWord:
                    return num_hops

                for neigh in adj_list[curr]:
                    if neigh not in visit:
                        visit.add(curr)
                        frontier.append(neigh)
                        
            num_hops += 1
        
        return 0

                
            

            

        