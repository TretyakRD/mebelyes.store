
vm = new Vue({
    el: '#app',
    data:{
        dist: 0,
        country:"",
        city: "",
        street: "",
        building: "",
    },
    methods: {
        calc: function () {
            let vm = this;
            $.ajax({
                url: "/map/calcdelv",
                data:{
                    from:"Муром",
                    to: vm.country+" "+vm.city+" "+vm.street+" "+vm.building,
                },
            }).then(function (dist) {
                if(dist!=="-1")
                    vm.dist = Number(dist.replace(/ /gi, ''))
            });
        }
    },
    delimiters: ['[[', ']]'],
});