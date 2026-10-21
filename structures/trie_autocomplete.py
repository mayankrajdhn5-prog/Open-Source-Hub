"""
Predictive autocomplete engine with weighted frequency ranking.
"""
class AutocompleteNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.weight = 0

class AutocompleteEngine:
    def __init__(self): self.root = AutocompleteNode()
    def insert(self, word: str, weight: int = 1):
        curr = self.root
        for ch in word:
            if ch not in curr.children: curr.children[ch] = AutocompleteNode()
            curr = curr.children[ch]
        curr.is_word = True
        curr.weight = max(curr.weight, weight)
    def suggest(self, prefix: str, limit: int = 5) -> list:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children: return []
            curr = curr.children[ch]
        results = []
        def _dfs(node, path):
            if node.is_word: results.append((node.weight, path))
            for ch, child in node.children.items(): _dfs(child, path + ch)
        _dfs(curr, prefix)
        results.sort(key=lambda x: x[0], reverse=True)
        return [w for _, w in results[:limit]]
