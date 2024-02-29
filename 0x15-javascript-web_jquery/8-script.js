const $ = window.$;
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.get(url, function (body) {
  const films = body.results;
  const list = $('#list_movies');
  films.forEach(element => {
    list.append('<li>' + element.title + '</li>\n');
  });
});
