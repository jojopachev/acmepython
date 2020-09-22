function dice(){
    return Math.floor(Math.random()*6)+1;
}

function init_clicked()
{
    var res = [];
    for (var i =0; i <= 10; i++) res.push(false);
    return res;
}

function is_valid_roll(arr, roll){
            
        }



new Vue({
    el: '#app',
    vuetify: new Vuetify(),
    data : {
        number: dice(),
        number2: dice(),
        boxs: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        player1_clicked: init_clicked(),
        player2_clicked: init_clicked(),
        selected: [],
        turn: true,
    },
    
    methods: {
         Roll_dice() {
             this.number = dice();
             this.number2 = dice();
             console.log("roll:",this.number, this.number2);
             this.turn = !this.turn;
        },
        
        Get_roll(){
            return this.number + this.number2;
        },
        
        Get_remaning() {
            let rem = [];
            for(i = 1; i <= 9; i++){
                if(!this.Get_clicked(i)){
                    rem.push(i);
                }
            }
            return rem;
        },
        
        Sum_boxes(num) {
                let sum_box = 0;
                this.selected.push(num);
                for(i = 0; i < this.selected.length; i++){
                    let b = this.selected[i];
                    if(this.Get_clicked(b)){
                        sum_box += b;
                    }
                }
                console.log(sum_box);
                if(this.number+this.number2 == sum_box){
                    this.selected = [];
                    this.Roll_dice();
                }
                else if(this.number+this.number2 < sum_box){
                    for(i = 0; i < this.selected.length; i++){
                        var box = this.selected[i];
                        this.Set_click(box, false)
                    }
                    console.log(":(");
                    this.selected = [];
                }
            console.log("sum:", sum_box,);
        },
        
        Get_player() {
            if(this.turn) return "Player1";
            
            else return "Player2";   
        },
        
        Get_clicked(num) {
            if(this.turn){
                return this.player1_clicked[num];
            }
            else {
                return this.player2_clicked[num]; 
            }
            
        },
        
        Set_click(num, val){
            if(this.turn){
                Vue.set(this.player1_clicked, num, val);
            }
            else{
                Vue.set(this.player2_clicked, num, val);
            }
        },
        
        Handle_click(player, num) {
            console.log(player, num);
            if(this.Get_clicked(num) && !this.selected.includes(num)){
                return;
            }
            if(player != this.Get_player()) return;
            this.Set_click(num, !this.Get_clicked(num));
            console.log("Remaning", this.Get_remaning());
            this.Sum_boxes(num);
        },
    }
});


/*import random
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
*/
