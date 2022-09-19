$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (req, res) {
    if (res === 'success') {
        $('#character').text(req.name);
    }
});