vm = new Vue({
    el: "#app",
    data: {
        name:'',
        prices:[],
        sizes:[],
        materials:[],
        img_url:'',
        cur_material:'',
        cur_size:'',
        cur_color:'',
        cur_price:''
    },
    methods: {
        toggle: function (g_id, b_id) {
            $('#'+g_id).find('.active').removeClass('active');
            $('#'+b_id).addClass('active');
            switch(g_id) {
                case "material":
                    this.cur_material=this.materials[b_id];
            }
        }
    },
    created: function () {
        let vm = this
        fetch(window.get_url).then(function (response) {
            return response.json()
        }).then(function (data) {
            vm.name = data[0].name;
            vm.prices = JSON.parse(data[0].prices);
            vm.sizes = JSON.parse(data[0].sizes);
            vm.materials = JSON.parse(data[0].material);
            vm.img_url = data[0].img_url;
        });
    },
    delimiters: ['[[',']]'],
});