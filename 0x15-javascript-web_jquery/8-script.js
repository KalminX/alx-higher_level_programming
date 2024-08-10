const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.get(url,
    function (data, textStatus, jqXHR) {
        console.log(data);
        let titles = data.results.map((result) => `<li>${result.title}</li>`)
        let titles_string = titles.join('');
        $('UL#list_movies').append(titles_string);
    },
    "json"
);