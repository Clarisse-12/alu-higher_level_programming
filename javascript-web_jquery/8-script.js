$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  $('ul#list_movies').append(data.results.map(film => `<li>${film.title}</li>`));
});
