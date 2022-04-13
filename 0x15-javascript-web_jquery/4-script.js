/**
 * Write a JavaScript script that toggles the class of the <header>
 * element when the user clicks on the tag DIV#toggle_header:
 * - The <header> element must always have one class: red or green,
 *   never both in the same time and never empty.
 * - If the current class is red, when the user click on DIV#toggle_header,
 *   the class must be updated to green ; and the reverse.
 * Please test with this HTML file 4-main.html
 */

const clicks = document.querySelector('DIV#toggle_header');
const header = document.querySelector('header');

clicks.addEventListener('click', () => {
  header.classList.toggle('green');
  header.classList.toggle('red');
});
