class Solution:
    def get_neighbor(self, word, wordList, visited):
        neighbors = list()
        for i, letter in enumerate(word):
            for l in "abcdefghijklmnopqrstuvwxyz":
                if letter == l: continue
                new_word = word[:i] + l + word[i+1:]
                if new_word in wordList and new_word not in visited:
                    neighbors.append(new_word)
                    visited.add(new_word)
        return neighbors

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordList = set(wordList)
        queue = collections.deque([(beginWord, 1)])
        visited = set()
        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            neighbors = self.get_neighbor(word, wordList, visited)
            for neighbor in neighbors:
                queue.append((neighbor, dist+1))
        return 0