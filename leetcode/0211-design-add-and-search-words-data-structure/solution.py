class WordDictionary:
    children: Dict[chr, Self]

    def __init__(self):
        self.children = {}
        
    def addWord(self, word: str) -> None:
        if not word:
            self.children[''] = None
            return
        c = word[0]
        if c not in self.children:
            new_trie = WordDictionary()
            new_trie.addWord(word[1:])
            self.children[c] = new_trie
        else:
            self.children[c].addWord(word[1:])

    def search(self, word: str) -> bool:
        if not word:
            return '' in self.children
        c = word[0]
        if c == '.':
            for c in self.children.keys():
                if c != '' and self.children[c].search(word[1:]):
                    return True
            return False
        elif c in self.children:
            return self.children[c].search(word[1:])
        else:
            return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
