const $ = window.$;
$(document).ready(function () {
  $('DIV#red_header').click(function () {
    // console.log('clicked')
    $('header').addClass('red');
  });
});
