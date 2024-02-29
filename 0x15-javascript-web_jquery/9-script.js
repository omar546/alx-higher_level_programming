const $ = window.$;
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$.get(url, function (body) {
  const hello = body.hello;
  $('#hello').html(hello);
});
