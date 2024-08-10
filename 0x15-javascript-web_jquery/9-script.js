const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";

$.get(url, function (data, textStatus, jqXHR) {
    console.log(data);
    $('DIV#hello').text(data.hello);
}, "json");
