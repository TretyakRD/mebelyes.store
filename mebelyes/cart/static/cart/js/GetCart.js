Vue.component('productincart', {
    props:['id', 'name', 'material', 'color', 'size', 'price'],
    data: function () {
        return {
            active: true,
        }
    },
    methods:{
        remove_cart: function () {
            this.active = false;
            this.$parent.total_price-=Number(this.price)
            var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
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
    template: `<tr v-if="active">
                                    <td>[[name]]</td>
                                    <td>[[material]]</td>
                                    <td>[[color]]</td>
                                    <td>[[size]]</td>
                                    <td>[[price]]</td>
                                    <td><button class="btn btn-danger btn-sm" @click="remove_cart">x</button></td>
                                </tr>`,
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