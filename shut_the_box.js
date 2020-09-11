function dice(){
    return Math.floor(Math.random()*6);
}

console.log(dice());

new Vue({
    el: '#app',
    vuetify: new Vuetify(),
    data : {
        number: dice(),
    }
});
