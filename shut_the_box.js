function dice(){
    return Math.floor(Math.random()*6)+1;
}

console.log(dice());

new Vue({
    el: '#app',
    vuetify: new Vuetify(),
    data : {
        number: dice(),
        number2: dice(),
        boxs: [1, 2, 3, 4, 5, 6, 7, 8, 9],
    }
});
