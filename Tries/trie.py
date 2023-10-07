class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfword = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfword = True

    def search(self, target: str) -> bool:
        cur = self.root
        
        for c in target:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfword

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True


obj = Trie()
obj.insert('chicken')
print(obj.search('chicken'))
print(obj.startsWith('chi'))
print(obj.search('eggs'))