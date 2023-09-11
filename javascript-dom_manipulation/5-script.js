// Get the element with id 'update_header' and the header element
var updateHeaderButton = document.getElementById('update_header');
var header = document.querySelector('header');

// Function to update the text of the header element
function updateHeader() {
  header.textContent = 'New Header!!!';
}

// Add a click event listener to the 'update_header' element
updateHeaderButton.addEventListener('click', updateHeader);

