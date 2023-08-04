const $ = window.$;
$(document).ready(function () {
  $.get("https://fourtonfish.com/hellosalut/?lang=fr", (data, textStatus) => {
    $("DIV#hello").text(data.hello);
  });
});i
