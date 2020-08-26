from collections import Counter
import time
start = time.time()


class Anagram(Counter):

    def __init__(self, word):
        Counter.__init__(self, word)
        self.word = word

    def __str__(self):
        return self.word


with open('words_alpha.txt') as file:
    words = file.readlines()
words = [i.rstrip().lower() for i in words]
words.sort(key=lambda x: len(x))


def match_word(word, letters):
    letters = letters.copy()
    for i in word:
        if letters[i] == 0:
            return False
        else:
            letters[i] -= 1
    return True


letters = 'drawncock'
letters = Anagram(letters)
valid_words = []
longest_words = []
second_longest_words = []
for word in words:
    if match_word(word, letters):
        valid_words.append(word)
        if not longest_words:
            longest_words.append(word)
        elif len(word) == len(longest_words[0]):
            longest_words.append(word)
        elif len(word) > len(longest_words[0]):
            second_longest_words = longest_words
            longest_words = []
            longest_words.append(word)
        if second_longest_words:
            if len(word) == len(second_longest_words[0]):
                second_longest_words.append(word)

print(f'Anagram: {letters}')
print(f'Total possible words: {len(valid_words)}')
print(f'Longest word(s): {" ".join(longest_words)}')
print(f'Longest word length: {len(longest_words[0])}')
print(f'Seconds longest words(s): {" ".join(second_longest_words)}')
print(f'Time taken: {time.time() - start}')
