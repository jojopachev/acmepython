import random
import numpy as np
import time
import plato

WHITE = 1
BLACK = 2


def play_game():
    g = PillarsOfPlato(width=4, length=4, height=5)
    while True:
        mes = g.get_mes()
        r = input(mes).split()
        try:
            g.move(int(r[0]), int(r[1]))
        except (ValueError, IndexError):
            print("Invalid input")
        g.print_heights()
        if g.game_over: return
        
def play_computer(color, mode):
    if mode == "Smart":
        a = plato.PlatoAI()
    else: a = None
        
    if color == "White":
        computer_turn = False
    else:
        computer_turn = True
        
    g = PillarsOfPlato(width=4, length=4, height=5)
    while True:
        if computer_turn:
                g.computer_move(mode, c=a)
        else:
            mes = g.get_mes()
            r = input(mes).split()
            try:
                g.move(int(r[0]), int(r[1]))
                #if a is not None:
                #    a.move(int(r[0]), int(r[1]))
            except (ValueError, IndexError):
                print("Invalid input")
                continue
        g.print_heights()
        computer_turn = not computer_turn
        if g.game_over: return
        
class PillarsOfPlato():
    
    def __init__(self, width=4, length=4, height=5, mute=False):
        self.heights = np.zeros((width, length),  dtype=int)
        self.board = np.zeros((width, length, height), dtype=int)
        self.turn = True
        self.game_over = False
        self.width = width
        self.height = height
        self.length = length
        self.last_move = None
        self.mute = mute
        random.seed(int(time.time()))
        
    def move(self,  x, y):
        self.board[x, y, self.heights[x, y]] = WHITE if self.turn else BLACK
        self.heights[x, y] += 1
        self.switch_turn()
        self.win()
        self.last_move = (x, y)
        
    def undo_move(self):
        x,y = self.last_move
        self.game_over = False
        self.switch_turn()
        self.heights[x, y] -= 1
        self.board[x, y, self.heights[x, y]] = 0
        
    def get_char(self, num):
        if num == 0: return "0"
        elif num == 1: return "W"
        else: return "B"

    def get_mes(self):
        if self.turn:
            return "White's turn:"
        else:
            return "Black's turn:"
            
    
    def print_heights(self):
        print(self.heights)
                
    def switch_turn(self):
        self.turn = not self.turn
        
    def win(self):
        ar1 = np.arange(4)
        ar2 = np.arange(4)
        ar3 = np.arange(4)
        ar4 = ar3[::-1]
        for i in range(self.width):
            self.check_board(self.board[i])
        for j in range(self.length):
            self.check_board(self.board[:, j])
        for k in range(self.height):
            self.check_board(self.board[:, :, k])
        self.check_board(self.board[ar1, ar2])
        self.check_board(self.board[ar3, ar4])
        
    def check_board(self, board):
        board = board.T
        height, width = board.shape
        xs = np.arange(4)
        ys = np.arange(4)        
        for i in range(height):
            self.check_slice(board[i])
        for j in range(width):
            for k in range(height - 3):
                self.check_slice(board[k:k+4, j])
        for l in range(height - width + 1):
            self.check_slice(board[xs + l, ys])
            self.check_slice(board[xs[::-1] + l, ys])

    def check_slice(self, ar):
        if self.game_over: return
        if np.all(ar == 1): 
            if not self.mute: print("White wins!")
            self.game_over = True
        elif np.all(ar == 2): 
            if not self.mute: print("Black wins!")
            self.game_over = True
        else: return
    
    def less_dumb_move(self):
        for x in range(self.width):
            for y in range(self.length):
                if self.heights[x, y] == self.height:
                    continue
                self.move(x, y)
                if self.game_over == True:
                    return
                else:
                    self.undo_move()
        self.rand_move()
            
        
    def smart_move(self, c):
        row, col = c.pick_move()
        self.move(row, col)
        
    def computer_move(self, mode, c=None):
        if mode == "Dumb":
            self.rand_move()
        elif mode == "Less dumb":
            self.less_dumb_move()
        elif mode == "Smart":
            if self.last_move is not None:
                x, y = self.last_move
                c.move(x, y)
            self.smart_move(c)
        else:
            print(f"Error {mode} is not a compatible mode")
    
    def rand_move(self):
        while True:
            rx = random.randint(0, 3)
            ry = random.randint(0, 3)
            if self.heights[rx, ry] == self.height:
                continue
            else:
                self.move(rx, ry)
                break

def test_game(moves):
    g = PillarsOfPlato(width=4, length=4, height=5)
    for m in moves:
        g.move(*m)
        print(g.check_board(g.board[:,0]))
        g.print_heights()
    return g
if __name__ == "__main__":
    #Horizontal win for White
    #g = test_game([[2, 2], [0, 0], [3, 3], [1, 0], [2, 2], [2, 0], [3, 3], [3, 0]])
    #test_game([[2, 2], [0, 0], [3, 3], [0, 0], [2, 2], [0, 0], [3, 3], [0, 0]])
    #test_game([[0, 0], [0, 0], [1, 1], [1, 0], [2, 2], [2, 0], [3, 3]])
    #test_game([[0,0], [0,0], [2, 2], [1,1], [1, 1], [2, 2], [2, 2],  [3,3], [3,3], [3, 3], [3, 3]])
    #print(g.check_board(g.board[:,0]))
    play_computer("White", "Smart")
