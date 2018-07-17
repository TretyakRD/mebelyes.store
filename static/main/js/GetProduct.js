Vue.component('serv', {
        props: ['service'],
        data: function(){
            return{
                price: 0,
                disable: true,
                active: false,
            }
        },
    methods:{
        set_price: function () {
            if(this.active){
                this.toggle()
            }
            this.price = this.service.prices[this.$parent.cur_material][this.$parent.cur_size];
            if(this.price){
                this.disable=false;
            }else{
                this.disable = true;
                this.active = false;
            }
        },
        toggle: function () {
            this.active = !this.active
            if (this.active)
                this.$parent.price+=Number(this.price);
            else
                this.$parent.price-=Number(this.price);
        },
    },
    created: function () {
      if(!(window.addsrvc))
          window.addsrvc=[]
        window.addsrvc.push(this)
    },
        template: `
        <tr>
            <td class="align-middle">
                [[ service.description ]]
            </td>
            <td class="align-middle">
                [[ price ]] ₽
            </td>
            <td>
                <button class="btn btn-outline-secondary rounded-circle border-white p-1" style="height:50px; width:50px " :disabled="disable" :class="{active : active}" @click="toggle"><i style="font-size:25px" class="far fa-check-circle text-center align-middle"></i></button>
            </td>
        </tr>
    `,
        delimiters: ['[[', ']]'],
    }
);


vm = new Vue({
    el: "#app",
    data: {
        id: '',
        name: '',
        prices: [],
        sizes: [],
        materials: [],
        colors: ["M-1", "M-2", "M-3", "M-4", "M-5", "M-6", "M-7", "M-8", "M-9", "M-10", "M-11", "M-12", "M-13", "M-13", "M-14", "M-15"],
        img_url: '',
        cur_material: '',
        cur_size: '',
        cur_color: '',
        category: '',
        cur_price: '',
        price: 0,
        services: [],
    },
    methods: {
        toggle: function (g_id, b_name) {
            $('#' + g_id).find(".active").removeClass("active");
            $('#' + g_id).find("[name=" + b_name + "]").addClass("active");
            switch (g_id) {
                case "material":
                    this.cur_material = b_name;
                    break;
                case "size":
                    this.cur_size = b_name;
                    break;
                case "color":
                    this.cur_color = b_name;
                    break;
            }
            this.set_price();
        },
        set_price: function () {
            this.$children.forEach(el=>{
                el.set_price()
            });
            this.price = this.prices[this.cur_material][this.cur_size];
        },
        add_to_cart: function () {
            vm = this;
            let srcs_arr=[];
            window.addsrvc.forEach(el=>{if(el.active)srcs_arr.push(el.service.id)});
            if (this.price != 0) {
                let csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
                jQuery.post("/cart/add", {
                    csrfmiddlewaretoken: csrftoken,
                    material: vm.materials.indexOf(vm.cur_material),
                    size: vm.sizes.indexOf(vm.cur_size),
                    color: this.cur_color,
                    category: this.category,
                    id: this.id,
                    name: this.name,
                    services: srcs_arr.toString(),
                }, function (data) {
                    console.log(data);
                });
            }
        },
    },
    created: function () {
        let vm = this
        fetch(window.get_url).then(function (response) {
            return response.json()
        }).then(function (data) {
            console.log(data);
            vm.id = data[0].id;
            vm.name = data[0].name;
            vm.prices = JSON.parse(data[0].prices.replace(/'/gi, '"'));
            vm.sizes = JSON.parse(data[0].sizes.replace(/'/gi, '"'));
            vm.materials = JSON.parse(data[0].material.replace(/'/gi, '"'));
            vm.img_url = data[0].img_url;
            vm.category = data[0].category;
            vm.services = data[0].services;
            vm.services.forEach(el => {
                el.prices = JSON.parse(el.prices);
            })
        });
    },
    delimiters: ['[[', ']]'],
});