import numpy as np

WHITE = 1
BLACK = 2

def play_game():
    g = ConnectFour(width=4, height=5s)
    while True:
        if g.turn:
            print("White's move:")
            g.move(int(input()))
            g.print_board()
            if g.game_over: return
        else:
            print("Black's move:")
            g.move(int(input()))
            g.print_board()
            if g.game_over: return

class ConnectFour():
    
    def __init__(self, width=4, height=5):
        self.heights = np.zeros(4, dtype=int)
        self.board = np.zeros((height, width), dtype=int)
        self.turn = True
        self.game_over = False
        self.width = width
        self.height = height

        
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
        for i in range(self.height):
            self.check_slice(self.board[i])
        for j in range(self.width):
            for k in range(self.height - 3):
                self.check_slice(self.board[k:k+4, j])

    def check_slice(self, ar):
        if np.all(ar == 1): 
            print("White wins!")
            self.game_over = True
        elif np.all(ar == 2): 
            print("Black wins!")
            self.game_over = True
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
    
