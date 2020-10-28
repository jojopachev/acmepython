import numpy as np

WHITE = 1
BLACK = 2

def play_game():
    g = PillarsOfPlato(width=4, length=4, height=5)
    while True:
        if g.turn:
            mes = "White's turn:"
            if g.game_over: return
        else:
            mes = "Black's turn:"
            if g.game_over: return
        r = input(mes).split()
        try:
            g.move(int(r[0]), int(r[1]))
        except (ValueError, IndexError):
            print("Invalid input")
        g.print_heights()
            
class PillarsOfPlato():
    
    def __init__(self, width=4, length=4, height=5):
        self.heights = np.zeros((width, length),  dtype=int)
        self.board = np.zeros((width, length, height), dtype=int)
        self.turn = True
        self.game_over = False
        self.width = width
        self.height = height
        self.length = length
        
    def move(self,  x, y):
        self.board[x, y, self.heights[x, y]] = WHITE if self.turn else BLACK
        self.heights[x, y] += 1
        self.switch_turn()
        self.win()
        
    def get_char(self, num):
        if num == 0: return "0"
        elif num == 1: return "W"
        else: return "B"

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
            print("White wins!")
            self.game_over = True
        elif np.all(ar == 2): 
            print("Black wins!")
            self.game_over = True
        else: return
        

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
    play_game()
