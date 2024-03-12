# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagrams):
        lowercase_word = self.word.lower()
        return [anagram for anagram in possible_anagrams if self._is_anagram(lowercase_word, anagram.lower())]

    def _is_anagram(self, word1, word2):
        return sorted(word1) == sorted(word2)