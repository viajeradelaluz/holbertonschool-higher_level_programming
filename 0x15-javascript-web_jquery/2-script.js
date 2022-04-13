/**
 * Write a JavaScript script that updates the text color of the <header> element
 * to red (#FF0000) when the user clicks on the tag DIV#red_header:
 * Please test with this HTML file 2-main.html
 */

// No JQuery
const clicks = document.querySelector("DIV#red_header");
const header = document.querySelector("header");

clicks.addEventListener("click", () => {
  header.style.color = "#FF0000";
});
