class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        from collections import deque

        word_set = set(wordList)
        q = deque([(beginWord,1)])

        while q :
            word,lvl = q.popleft()
            if word == endWord : return lvl
            for idx in range(len(word)):
                ori_char = word[idx]
                for char in range(ord('a'),ord('z') + 1):
                    chars = list(word)
                    chars[idx] = chr(char)
                    new_word = ''.join(chars)
                    if new_word in word_set :
                        q.append((new_word,lvl + 1))
                        word_set.remove(new_word)

        return 0

            
                    

        