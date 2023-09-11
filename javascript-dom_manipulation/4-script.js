// Get the elements with id 'add_item' and the ul element with class 'my_list'
var addItemButton = document.getElementById('add_item');
var myList = document.querySelector('.my_list');

// Function to add a new li element to the ul
function addItemToList() {
  // Create a new li element
  var newLi = document.createElement('li');
  // Set the text content of the new li element
  newLi.textContent = 'Item';
  // Append the new li element to the ul
  myList.appendChild(newLi);
}

// Add a click event listener to the 'add_item' element
addItemButton.addEventListener('click', addItemToList);
