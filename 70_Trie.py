'''208. Implement Trie (Prefix Tree)'''
class Trie:
    def __init__(self):
      self.root=[]

    def insert(self, word: str) -> None:
      self.root.append(word)
      return None      

    def search(self, word: str) -> bool:
      return word in self.root

    def startsWith(self, prefix: str) -> bool:
        for word in self.root:
          if word.startswith(prefix):return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)