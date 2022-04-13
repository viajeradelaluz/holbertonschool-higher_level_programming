/**
 * Write a JavaScript script that adds the class red to the <header>
 * element when the user clicks on the tag DIV#red_header.
 * Please test with this HTML file 3-main.html
 */

// No JQuery
const header = document.querySelector('header');
const clicks = document.querySelector('DIV#red_header');

clicks.addEventListener('click', () => {
  header.setAttribute('class', 'red');
});
