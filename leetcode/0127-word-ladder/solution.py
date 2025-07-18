class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        q = deque([(beginWord, 1)])
        if beginWord in wordSet:
            wordSet.remove(beginWord)
        while q:
            (word, steps) = q.popleft()
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    nextWord = word[:i] + c + word[i + 1:]
                    if nextWord == endWord:
                        return steps + 1
                    if nextWord in wordSet:
                        wordSet.remove(nextWord)
                        q.append((nextWord, steps + 1))
        return 0

