import random
import sys
import box
import time

s = {1,2,3,4,5,6,7,8,9}
total_time = sys.argv[(1)]
start_time = time.time()

def dice():
    return random.randint(2, 12)

def real_dice():
    return random.randint(1, 6)

def print_time():
    time_left = int(sys.argv[(1)]) - time.time() + start_time
    if time_left < 0:
        print("Ha ha, you ran out of time :P")
        sys.exit(1)
    print("Time remaining:", round(time_left, 2))
    
def shut_the_box():
    print("Numbers left:", s)
    roll = real_dice() + real_dice() if sum(s) > 6 else real_dice()
    print("Roll:", roll)
    print_time()
    if not box.isvalid(roll, s):
        print("Ha ha, you lose sucker :P")
        return False
    res = input("Numbers to eliminate:")
    nums = box.parse_input(res, s)
    while sum(nums) != roll:
        print("Invalid input!")
        res = input("Numbers to eliminate:")
        nums = box.parse_input(res, s)
    for i in nums:
        s.remove(i)
    if not len(s):
        print("Wow! How'd someone like you manage to win this game")
        return False
    return True

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error! Username and time limit required")
        sys.exit(1)
        
    while shut_the_box(): pass
    print(f"Score for {sys.argv[(2)]}:", sum(s))
    print_time()
