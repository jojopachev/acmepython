import random
import box

s = {1,2,3,4,5,6,7,8,9}

def dice():
    return random.randint(2, 12)

def real_dice():
    return random.randint(1, 6)

def shut_the_box():
    print("Numbers left:", s)
    roll = real_dice() + real_dice() if sum(s) > 6 else real_dice()
    print("Roll:", roll)
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
    while shut_the_box(): pass
    print("your score:", sum(s))
