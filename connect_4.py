import numpy as np

WHITE = 1
BLACK = 2
width = 4
height = 5

def play_game():
    g = ConnectFour()
    while True:
        if g.turn:
            print("White's move:")
            g.move(int(input()))
            g.print_board()
        else:
            print("Black's move:")
            g.move(int(input()))
            g.print_board()

class ConnectFour():
    
    def __init__(self):
        self.heights = np.zeros(4, dtype=int)
        self.board = np.zeros((5, 4), dtype=int)
        self.turn = True
        
    def move(self,  pos):
        self.board[self.heights[pos], pos] = WHITE if self.turn else BLACK
        self.heights[pos] += 1
        self.switch_turn()
        self.win()

    def print_board(self):
        print(self.board[::-1])
    
    def switch_turn(self):
        self.turn = not self.turn
    
    def win(self):
        for i in range(height):
            if np.all(self.board[i] == 1): print("White wins!") 
            elif np.all(self.board[i] == 2): print("Black wins!")
            else: return

if __name__ == "__main__":
    #game = ConnectFour()
    #game.move(2)
    #game.switch_turn()
    #game.move(0)
    #game.switch_turn()
    #game.move(2)
    #game.move(2)
    #game.move(2)
    #game.switch_turn()
    #game.move(1)
    #game.move(1)  
    #game.move(1)
    play_game()
    
