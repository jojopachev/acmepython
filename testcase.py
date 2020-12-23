import pillars as  p
import plato

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
    m = 0
    a = b = None
    if white_mode  == "Smart":
        a = plato.PlatoAI()
    if black_mode == "Smart":
        b = plato.PlatoAI()
        
    g = p.PillarsOfPlato(width=4, length=4, height=5, mute=mute)
    move = []
    while True:
        m += 1
        if g.turn: 
            g.computer_move(white_mode, c=a)
        else:
            g.computer_move(black_mode, c=b)
        move.append(g.last_move)
        if m == 80:
            winner = 0
            break
        if g.game_over:
            if g.turn:
                winner = 2
            else:
                winner = 1
            break
    return move, winner

def ai_battle(depth1 = 2, depth2 = 2):
    moves = []
    winner = 0
    a = plato.PlatoAI()
    b = plato.PlatoAI()
    a.set_depth(depth1)
    b.set_depth(depth2)
    for m in range(1, 81):
        if m%2 == 1:
            us, them = a, b
        else:
            us, them = b, a
        move = us.pick_move()
        moves.append(move)
        x,y = move
        them.move(x, y)
        if us.game_over():
            if m%2 == 0:
                winner = 2
            else:
                winner = 1
            break
    return moves, winner
    
def make_testcase(fname):
    move, winner = play_game("Smart", "Smart")
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
    print_stats = lambda: print(f"Average Game Length: {np.mean(lengths[:i+1])}, White win: {100*np.mean(winners[:i+1]==1)}", f"Black win: {100*np.mean(winners[:i+1]==2)}", f"Draw: {100*np.mean(winners[:i+1]==0)}")

    for i in range(n):
        #move, winner = play_game("Dumb", "Less dumb", mute=True)
        #move, winner = play_game("Less dumb", "Dumb", mute=True)
        #move, winner = play_game("Less dumb", "Less dumb", mute=True)
        #move, winner = play_game("Smart", "Smart", mute=True)
        move, winner = ai_battle(2,1)
        lengths[i] = len(move)
        winners[i] = winner
        if i%100 == 0: print(f"Processed {i+1}")
        if i %1000 == 0: print_stats()
    print_stats()

if __name__ == "__main__":
    #make_testcases(50)
    get_stats(250)
    #print(ai_battle(2, 2))
