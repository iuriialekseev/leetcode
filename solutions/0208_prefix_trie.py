class TrieNode:

    def __init__(self):
        self.nodes = dict()
        self.is_last = False

class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.nodes:
                curr.nodes[c] = TrieNode()
            curr = curr.nodes[c]
        curr.is_last = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.nodes:
                return False
            curr = curr.nodes[c]
        return curr.is_last


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.nodes:
                return False
            curr = curr.nodes[c]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
