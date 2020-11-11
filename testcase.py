import pillars as  p

def random_game(mute=False):
    g = p.PillarsOfPlato(width=4, length=4, height=5, mute=mute)
    move = []
    while True:
        g.rand_move()
        #print(g.last_move)
        move.append(g.last_move)
        if g.game_over:
            if g.turn:
                winner = 2
            else:
                winner = 1
            #print(winner)
            break
    return move, winner

def play_game(white_mode, black_mode, mute=False):
    g = p.PillarsOfPlato(width=4, length=4, height=5, mute=mute)
    move = []
    while True:
        if g.turn: 
            g.computer_move(white_mode)
        else:
            g.computer_move(black_mode)
        move.append(g.last_move)
        if g.game_over:
            if g.turn:
                winner = 2
            else:
                winner = 1
            break
    return move, winner

def make_testcase(fname):
    move, winner = play_game("Dumb", "Less dumb")
    with open(fname, "w") as f:
            f.write(str(winner) + "\n")
            for t in move:
                f.write(" ".join(map(str, t)) + "\n")

def make_testcases(n):
    for i in range(n):
        make_testcase(f"josephplatotests/test{i}.txt")

def get_stats(n):
    import numpy as np
    lengths = np.zeros(n)
    winners = np.zeros(n)
    i = 0
    print_stats = lambda: print(f"Average Game Length: {np.mean(lengths[:i+1])}, White win: {100*np.mean(winners[:i+1]==1)}")

    for i in range(n):
        #move, winner = play_game("Dumb", "Less dumb", mute=True)
        #move, winner = play_game("Less dumb", "Dumb", mute=True)
        move, winner = play_game("Less dumb", "Less dumb", mute=True)
        lengths[i] = len(move)
        winners[i] = winner
        if i%10 == 0: print(f"Processed {i+1}")
        if i %100 == 0: print_stats()
    print_stats()

if __name__ == "__main__":
    #make_testcases(50)
    get_stats(500)
