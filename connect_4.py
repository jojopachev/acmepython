import numpy as np

WHITE = 1
BLACK = 2

def play_game():
    g = ConnectFour(width=4, height=5)
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
        
    def get_char(self, num):
        if num == 0: return "0"
        elif num == 1: return "W"
        else: return "B"

    def print_board(self):
        for i in range(self.height -1, -1, -1):
            a = []
            for j in range(self.width):
                a.append(self.get_char(self.board[i, j]))
            print(" ".join(a))
                
    def switch_turn(self):
        self.turn = not self.turn
    
    def win(self):
        xs = np.arange(4)
        ys = np.arange(4)
        for i in range(self.height):
            self.check_slice(self.board[i])
        for j in range(self.width):
            for k in range(self.height - 3):
                self.check_slice(self.board[k:k+4, j])

        for l in range(self.height - self.width + 1):
            self.check_slice(self.board[xs + l, ys])
            self.check_slice(self.board[xs[::-1] + l, ys])

    def check_slice(self, ar):
        if self.game_over: return
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
    
