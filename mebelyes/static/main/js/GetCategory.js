vm = new Vue({
    el: "#app",
    data: {
        products: [],
    },
    methods: {
        get_url: function (idd) {
            return window.get_p_url+idd
        }
    },
    created: function () {
        let vm = this
        fetch(window.get_c_url).then(function (response) {
            return response.json()
        }).then(function (data) {
            vm.products = data;
        });
    },
    delimiters: ['[[',']]'],
});