const url = "https://swapi-api.alx-tools.com/api/people/5/?format=json";

$.get(
  url,
  function (data) {
    console.log(data);
    $("DIV#character").text(data.name);
  },
  "json"
);
