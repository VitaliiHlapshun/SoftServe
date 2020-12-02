class Gallows:

    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, word):
        if self.game_over:
            return "game over"
        if self.is_word_valid(word):
            self.words.append(word)
            return self.words
        else:
            self.game_over = True
            return "game over"

    def is_word_valid(self, word: str):
        if not self.words:
            return True
        letter_to_check = self.words[-1][-1]
        if word in self.words or not word.startswith(letter_to_check):
            return False
        return True

    def restart(self):
        self.game_over = False
        self.words = []
        return "game restarted"

a = Gallows()
print(a.play('apple'))
print(a.play('ear'))
print(a.play('row'))
print(a.play('arid'))
print(a.play('apple'))
print(a.restart())
print(a.play('ear'))
print(a.play('row'))
print(a.play('row'))
