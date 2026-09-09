class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        from collections import deque
        from collections import defaultdict
        q=deque([(beginWord,1)])
        wordset=set(wordList)
        visi={beginWord}
        parents=defaultdict(list)
        ps="pqowieurtyalskdjhfgzmnxbcv"
        dist={beginWord:1}
        while q:
            word,st=q.popleft()
            
            for ch in ps:
                for i in range(len(word)):
                    nword=word[:i]+ch+word[i+1:]
                    if nword in wordset:
                        if nword not in visi:
                            visi.add(nword)
                            q.append((nword,st+1))
                            dist[nword]=st+1
                            parents[nword].append(word)
                        elif dist[nword]==st+1:
                            parents[nword].append(word)
        dvisi=set()
        def dfs(s,res):
            if s==beginWord:
                k.append(res[::-1])
                return
            for neib in parents[s]:
                dfs(neib,res+[neib])
        k=[]
        dfs(endWord,[endWord])
        
        return k
