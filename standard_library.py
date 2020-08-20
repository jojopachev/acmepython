from itertools import combinations
import calculator

def list_stuff(el_list):
    Min = min(el_list)
    Max = max(el_list)
    avg = (sum(el_list))/len(el_list)
    print(f"min = {Min}, max = {Max}, average = {avg} " )
    
def mutable_checker():
    Int = 1
    Int2 = Int
    Int2 = 2
    if Int == Int2:
        print("true")
    else:
        print("false")
    
    Str = "1"
    Str2 = Str
    Str2 = "12"
    if Str == Str2:
        print("true")
    else:
        print("false")
        
    List = [1,2,3,4]
    List2 = List
    List2.append(5)
    if List == List2:
        print("true")
    else:
        print("false")
        
    Tuple = (1,2,3,4)
    Tuple2 = Tuple
    Tuple2 += (1,)
    if Tuple == Tuple2:
        print("true")
    else:
        print("false")
        
    Set = {1,2,3,4}
    Set2 = Set
    Set2.add(5)
    if Set == Set2:
        print("true")
    else:
        print("false")
        
def triangle(a, b):
    return calculator.Sqrt(calculator.add(calculator.product(a, a), calculator.product(b, b)))
    
def power_set(A):
    l = []
    for i in range(len(A)+1):
        for t in combinations(A, i):
            l.append(set(t))
    return l
        
if __name__ == "__main__":
    l = {"a", "b", "c"}
    #print(triangle(3, 4))
    print(power_set(l))
