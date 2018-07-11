Vue.component('productincart', {
    props:['id', 'name', 'material', 'color', 'size', 'price', 'services'],
    data: function () {
        return {
            active: true,
        }
    },
    methods:{
        remove_cart: function () {
            this.active = false;
            this.$parent.total_price-=Number(this.price);
            this.services.forEach(i=>{
                this.$parent.total_price-=Number(i.price)
            });
            let csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
            jQuery.post("/cart/remove",{
                csrfmiddlewaretoken: csrftoken,
                num: {
                    'id':this.id,
                    'name':this.name,
                    'material':this.material,
                    'color':this.color,
                    'size':this.size,
                    'price':this.price,
                },
            }, function(data){
                console.log(data);
            });
        },
    },
    template: `
<div class="container-fluid px-0" v-if="active">
<div class="row py-4 border">
<div class="col-2">
[[ name ]]
</div>
<div class="col-2">
[[ material ]]
</div>
<div class="col-2">
[[ color ]]
</div>
<div class="col-2">
[[ size ]]
</div>
<div class="col-2">
[[ price ]]
</div>
<div class="col-2">
<button class="btn btn-danger btn-sm" @click="remove_cart">x</button>
</div>
</div>
<div class="row py-4 border" v-for="srv in services">
<div class="col-2">

</div>
<div class="col-6">
[[srv.description]]
</div>
<div class="col-2">
[[srv.price]]
</div>
<div class="col-2">
</div>
</div>
</div>
`,
    delimiters: ['[[', ']]'],
});
vm = new Vue({
    el: "#app",
    data: {
        cart: [],
        total_price: 0,
    },
    created: function () {
        this.cart = JSON.parse(window.cart.replace(/'/gi, '"'));
        this.total_price = window.total_price;
    },
    methods: {

    },
    delimiters: ['[[', ']]'],
});