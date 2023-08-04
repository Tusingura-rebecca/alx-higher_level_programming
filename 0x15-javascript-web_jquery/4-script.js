const $ = window.$;
$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
    // console.log('clicked')
    $('header').toggleClass('red green');
  });
});
