/**
 * Write a JavaScript script that adds, removes and clears LI elements from a list when the user clicks:
 * - The new element must be: <li>Item</li>
 * - The new element must be added to UL.my_list
 * - When the user clicks on DIV#add_item: a new element is added to the list
 * - When the user clicks on DIV#remove_item: the last element is removed from the list
 * - When the user clicks on DIV#clear_list: all elements of the list are removed
 * - You can’t use document.querySelector to select the HTML tag
 * - You script must work when it imported from the HEAD tag
 * Please test with this HTML file 101-main.html
 */

window.onload = () => {
  const $ulList = document.querySelector('.my_list');
  const $addItem = document.querySelector('#add_item');
  const $removeItem = document.querySelector('#remove_item');
  const $clearList = document.querySelector('#clear_list');
  $addItem.addEventListener('click', addItem($ulList));
  $removeItem.addEventListener('click', removeItem($ulList));
  $clearList.addEventListener('click', removeItem($ulList, true));
};

const addItem = ($ulList) => () => {
  const $newItem = document.createElement('li');
  $newItem.textContent = 'Item';
  $ulList.appendChild($newItem);
};

const removeItem = ($ulList, clear = false) => () => {
  const lastChild = $ulList.lastChild;
  if (!lastChild) return;
  $ulList.removeChild(lastChild);
  if (clear) removeItem($ulList, true)($ulList);
};
