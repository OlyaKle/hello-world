class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def backtrack(index, letter_count, curr_sum):
            if index == len(words):
                self.ans = max(self.ans, curr_sum)
                return

            word = words[index]
            temp = letter_count[:]
            curr_word_sum = 0
            valid = True
            for c in word:
                if letter_count[ord(c) - 97] == 0:
                    valid = False
                    break
                curr_word_sum += score[ord(c) - 97]
                letter_count[ord(c) - 97] -= 1
            if valid:
                backtrack(index + 1, letter_count, curr_sum + curr_word_sum)
            letter_count = temp[:]
            backtrack(index + 1, letter_count, curr_sum)

        letter_count = [0] * 26
        for c in letters:
            letter_count[ord(c) - 97] += 1

        self.ans = 0
        backtrack(0, letter_count, 0)
        return self.ans