/**
 * Write a JavaScript script that updates the text of the <header> element
 * to New Header!!! when the user clicks on DIV#update_header.
 * Please test with this HTML file 6-main.html
 */

const updateHeader = document.querySelector('#update_header');
const header = document.querySelector('header');

updateHeader.addEventListener('click', () => {
  header.innerText = 'New Header!!!';
});
