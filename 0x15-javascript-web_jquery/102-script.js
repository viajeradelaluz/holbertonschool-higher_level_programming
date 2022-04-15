/**
 * Write a JavaScript script that fetches and prints how to say “Hello” depending on the language
 * - You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
 * - The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
 * - The translation must be fetched when the user clicks on INPUT#btn_translate
 * - The translation of “Hello” must be displayed in the HTML tag DIV#hello
 * - You script must work when imported from the <head> tag
 * Please test with this HTML file 102-main.html
 */

window.onload = () => {
  const $lang = document.querySelector('#language_code');
  const $translate = document.querySelector('#btn_translate');
  const $hello = document.querySelector('#hello');
  $translate.addEventListener('click', newHello($lang, $hello));
};

const url = 'https://fourtonfish.com/hellosalut/?lang=';

const newHello = ($lang, $hello) => () => {
  fetch(`${url}${$lang.value}`)
    .then(response => response.json())
    .then(data => {
      $hello.textContent = data.hello;
    });
};
