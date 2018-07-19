
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
                    from:"Россия Москва ул. Софийская набережная 26/1",
                    to: vm.country+" "+vm.city+" "+vm.street+" "+vm.building,
                },
            }).then(function (dist) {
                if(dist!=="-1")
                    vm.dist = Number(dist.replace(/ /gi, '').replace(/,/gi, '.'))
                if(vm.dist<30)
                    vm.dist=0
            });
        }
    },
    delimiters: ['[[', ']]'],
});