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
        if(roll < 0) return false;
        if(roll == 0) return true;
        if(arr.length == 1){
            return arr[0] == roll;
        }
        return is_valid_roll(arr.slice(1,), roll-arr[0]) || is_valid_roll(arr.slice(1,), roll);
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
        player1_dead: false,
        player2_dead: false,
        score1:50,
        score2:50,
        time:60,
        time1:null,
        time2:null,
        gameInProgress:false,
    },
    
    methods: {
         Roll_dice() {
            this.Score();
            if (this.turn && !this.score1) this.Kill("Player1");
            else if (!this.turn && !this.score2) {
                this.Kill("Player2");
                this.Kill("Player1");
            }
            console.log(this.time);
            console.log("roll", this.Get_roll()) 
            this.turn = !this.turn;
            if(this.Check_dead()){ 
                this.turn = !this.turn;
                if(this.Check_dead()) return; 
            }
            while (true) {
                this.number = dice();
                this.number2 = (this.Get_score() > 6) ? dice() : 0;
                var res = is_valid_roll(this.Get_remaining(), this.Get_roll());
                //if (!this.turn && !res) continue;
                break;
            }
            if(!res) {
                this.Kill(this.Get_player());
                setTimeout(this.Roll_dice, 2000);
                this.Score();
            }
        },
        Get_winner(){
            if(this.score1 < this.score2) return "Player1 wins";
            else if(this.score1 == this.score2) return "Draw"; 
            else return "Player2 wins";
        },
        
        Score() {
            let s = 0;
            let l = this.Get_remaining().length;
            let a = this.Get_remaining();
            for(i = 0; i < l; i++){
                s += a[i];
                console.log(s);
            }
            if(this.turn) this.score1 = s;
            else this.score2 = s;
            console.log('score 1', this.score1, "score2", this.score2);
        },
        
        Get_score() {
            return (this.turn) ? this.score1 : this.score2;
        },
        
        Get_roll(){
            return this.number + this.number2;
        },
        
        Get_remaining() {
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
        
        Timer(){
            this.time1 = this.time;
            this.time2 = this.time;
            if(this.turn){
              if(this.time > 0) {
                    setTimeout(() => {
                        if (this.time1 <= 0) return;
                        this.time1 -= 1;
                        this.Timer();
                    }, 1000)
                }  
            }
        },
        
        StartGame(){
            if(this.gameInProgress) return;
            this.Timer();
            this.gameInProgress = true;
        },
        
        Set_click(num, val){
            if(this.turn){
                Vue.set(this.player1_clicked, num, val);
            }
            else{
                Vue.set(this.player2_clicked, num, val);
            }
        },
        
        Kill(player){
            console.log("Killing "+player);
            if(player == "Player1") this.player1_dead = true;
            else this.player2_dead = true;
        },
        
        Check_dead() {
            return (this.turn) ? this.player1_dead : this.player2_dead;
        },
        
        Handle_click(player, num) {
            console.log(player, num);
            if(this.Get_clicked(num) && !this.selected.includes(num)){
                return;
            }
            if(player != this.Get_player()) return;
            this.Set_click(num, !this.Get_clicked(num));
            this.Sum_boxes(num);
        },
    }
});
