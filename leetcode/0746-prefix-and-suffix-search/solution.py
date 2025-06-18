class Trie:
    children: Dict[chr, Self]
    index = Optional[int]

    def __init__(self, index = None):
        self.children = {}
        self.index = index
        
    def insert(self, word: str, index: int) -> None:
        if not word:
            self.children[''] = Trie(index)
            return
        c = word[0]
        if c not in self.children:
            new_trie = Trie()
            new_trie.insert(word[1:], index)
            self.children[c] = new_trie
        else:
            self.children[c].insert(word[1:], index)

    def search(self, word: str) -> bool:
        if not word:
            return '' in self.children
        c = word[0]
        if c in self.children:
            return self.children[c].search(word[1:])
        else:
            return False

    def startsWith(self, prefix: str) -> Optional[Self]:
        if not prefix:
            return self
        c = prefix[0]
        if c in self.children:
            return self.children[c].startsWith(prefix[1:])
        else:
            return None
    
    def largest_index(self) -> int:
        mx = self.index if self.index is not None else -1
        if self.children:
            mx = max(mx, max(child.largest_index() for child in self.children.values()))
        return mx
        


class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for i, word in enumerate(words):
            for suffix_start in range(0, len(word) + 1):
                w = word[suffix_start:] + "|" + word
                print(w)
                self.trie.insert(w, i)

    def f(self, pref: str, suff: str) -> int:
        found = self.trie.startsWith(suff + "|" + pref)
        if not found:
            return -1
        return found.largest_index()
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
