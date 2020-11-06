import pillars as  p

def make_testcase(fname):
    g = p.PillarsOfPlato(width=4, length=4, height=5)
    while True:
        g.rand_move()
        print(g.last_move)
        with open(fname, "w") as f:
            f.write(str(g.last_move))
        
        if g.game_over:
            if g.turn:
                winner = 2
            else:
                winner = 1
            print(winner)    
            return
        
if __name__ == "__main__":
    make_testcase("test")
