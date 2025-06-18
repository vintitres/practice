class Trie:
    children: Dict[chr, Self]

    def __init__(self):
        self.children = {}
        
    def insert(self, word: str) -> None:
        if not word:
            self.children[''] = None
            return
        c = word[0]
        if c not in self.children:
            new_trie = Trie()
            new_trie.insert(word[1:])
            self.children[c] = new_trie
        else:
            self.children[c].insert(word[1:])

    def search(self, word: str) -> bool:
        if not word:
            return '' in self.children
        c = word[0]
        if c in self.children:
            return self.children[c].search(word[1:])
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        c = prefix[0]
        if c in self.children:
            return self.children[c].startsWith(prefix[1:])
        else:
            return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
