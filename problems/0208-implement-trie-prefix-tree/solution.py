class TreeNode:
    def __init__(self, val = "", children = None):
        self.val = val
        self.children = {} if children is None else children
        self.wordend = False

class Trie:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = TreeNode(val = word[i])
            curr = curr.children[word[i]]
        curr.wordend = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            if word[i] in curr.children:
                curr = curr.children[word[i]]
            else:
                return False
        
        return curr.wordend
            

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        print(curr.children)
        for i in range(len(prefix)):
            if prefix[i] in curr.children:
                curr = curr.children[prefix[i]]
            else:
                return False

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
