import os
import random
import oxo_data

class Game:
    def __init__(self):
        self.board = [" " for _ in range(9)]

    def saveGame(self):
        oxo_data.saveGame(self.board)

    def restoreGame(self):
        try:
            restored_board = oxo_data.restoreGame()
            if len(restored_board) == 9:
                self.board = restored_board
            else:
                self.board = [" " for _ in range(9)]
        except IOError:
            self.board = [" " for _ in range(9)]

    def _generateMove(self):
        options = [i for i, cell in enumerate(self.board) if cell == " "]
        return random.choice(options) if options else -1

    def _isWinningMove(self):
        wins = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        )

        for a, b, c in wins:
            chars = self.board[a] + self.board[b] + self.board[c]
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False

    def userMove(self, cell):
        if self.board[cell] != ' ':
            raise ValueError('Invalid cell')
        
        self.board[cell] = 'X'
        return 'X' if self._isWinningMove() else ""

    def computerMove(self):
        cell = self._generateMove()
        if cell == -1:
            return 'D'  # Draw

        self.board[cell] = 'O'
        return 'O' if self._isWinningMove() else ""

    def displayBoard(self):
        for row in range(0, 9, 3):
            print(self.board[row:row+3])

def test():
    result = ""
    game = Game()
    while not result:
        game.displayBoard()
        try:
            result = game.userMove(game._generateMove())
        except ValueError:
            print("Oops, that shouldn't happen")

        if not result:
            result = game.computerMove()

        if result:
            if result == 'D':
                print("It's a draw!")
            else:
                print("Winner is:", result)
            game.displayBoard()

if __name__ == "__main__":
    test()
