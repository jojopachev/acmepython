import numpy as np

WHITE = 1
BLACK = 2

class ConnectFour():
    
    def __init__(self):
        self.heights = np.zeros(4, dtype=int)
        self.board = np.zeros((5, 4), dtype=int)
        self.turn = True
        
    def move(self,  pos):
        self.board[self.heights[pos], pos] = WHITE if self.turn else BLACK
        self.heights[pos] += 1

    def print_board(self):
        print(self.board[::-1])
    
    def switch_turn(self):
        self.turn = not self.turn

if __name__ == "__main__":
    game = ConnectFour()
    game.move(2)
    game.switch_turn()
    game.move(0)
    game.switch_turn()
    game.move(2)
    game.move(2)
    game.move(2)
    game.switch_turn()
    game.move(1)
    game.move(1)  
    game.move(1)
    game.print_board()
