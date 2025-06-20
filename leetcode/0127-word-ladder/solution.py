class Solution:
    def nextWords(self, word: str):
        for i in range(len(word)):
            for c in (chr(x) for x in range(ord('a'), ord('z') + 1)):
                yield word[:i] + c + word[i + 1:]

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        seen = set([beginWord])
        q = deque([(beginWord, 1)])
        while q:
            (word, steps) = q.popleft()
            print('w', word)
            for nextWord in self.nextWords(word):
                if nextWord == endWord:
                    return steps + 1
                if nextWord in wordSet and nextWord not in seen:
                    seen.add(nextWord)
                    q.append((nextWord, steps + 1))
        return 0

