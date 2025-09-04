class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.eow = True

    def search(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.eow

    def startsWith(self, prefix):
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.add("Savio")
    trie.add("Sav")
    trie.add("Svo")
    print(trie.search("Savio"))
    print(trie.startsWith("Svi"))
