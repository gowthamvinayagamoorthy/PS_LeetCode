class Solution:
    def ladderLength(self, beginword: str, endword: str, wordList: List[str]) -> int:
        if endword not in wordList:
            return 0
        wordset=set(wordList)
        from collections import deque
        visi={beginword}
        ps="qwertyuioplkjhgfdsazxcvbnm"
        q=deque([(beginword,1)])
        while q:
            word,st=q.popleft()
            if word==endword:
                return st
            for ch in ps:
                for i in range(len(word)):
                    newword=word[:i]+ch+word[i+1:]
                    if newword in wordset and newword not in visi:
                        visi.add(newword)
                        q.append((newword,st+1))
        return 0