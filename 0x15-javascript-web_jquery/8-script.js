// https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/for...of
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (req, res) {
    if (res === 'success') {
        for (let film of req.results) {
            $('#list_movies').append($('<li></li>').text(film.title));
        }
    }
});