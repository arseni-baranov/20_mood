jokes = {{ jokes_json }};

amount = jokes.length - 1;
random = Math.floor((Math.random() * amount) + 1);

$('h2#joke_text').html(jokes[random]['elementPureHtml']);
$('p#site').text(jokes[random]['name']);