from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True


    def search(self, word: str) -> bool:
        queue = deque([(self.root, 0)])

        while queue:
            node, i = queue.popleft()
            if i == len(word):
                if node.is_end:
                    return True
                continue

            c = word[i]
            if c == '.':
                for child in node.children.values():
                    queue.append((child, i + 1))
            elif c in node.children:
                queue.append((node.children[c], i + 1))

        return False
