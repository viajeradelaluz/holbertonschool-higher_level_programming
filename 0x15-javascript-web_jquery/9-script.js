/**
 * Write a JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr
 * and displays the value of hello from that fetch in the HTML tag DIV#hello.
 * - The translation of “hello” must be displayed in the HTML tag DIV#hello
 * - You can’t use document.querySelector to select the HTML tag
 * - Your script must work when it is imported from the <head> tag
 * Please test with this HTML file 9-main.html
 */

window.onload = () => {
  const $hello = document.querySelector('#hello');
  $hello = newHello($hello);
};

const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

const newHello = ($hello) => {
  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      $hello.textContent = data.hello;
    });
};
