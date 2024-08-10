$(function () {
  const url = "https://www.fourtonfish.com/hellosalut/hello/";

  $.get(
    url,
    function (data, textStatus, jqXHR) {
      console.log(data);
    },
    "json"
  );
});
