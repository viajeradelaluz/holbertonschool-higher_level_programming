/**
 * Write a JavaScript script that adds a <li> element to a list when the user clicks on
 * the tag DIV#add_item:
 * - The new element must be: <li>Item</li>
 * - The new element must be added to UL.my_list
 */

window.onload = () => {
  const $addItem = document.querySelector('#add_item');
  const $ulList = document.querySelector('UL.my_list');
  $addItem.addEventListener('click', addItem($ulList));
};

const addItem = ($ulList) => () => {
  const $newItem = document.createElement('LI');
  $newItem.textContent = 'Item';
  $ulList.appendChild($newItem);
};
