fetch(window.get_url).then(function (response) {
    return response.data.json()
}).then(function (data) {
        console.log(data);
    $('app').html(data);
});