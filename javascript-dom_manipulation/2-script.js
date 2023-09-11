// Get the elements with id 'red_header' and 'header'
var redHeader = document.getElementById('red_header');
var header = document.querySelector('header');

// Function to add the 'red' class to the header element when clicked
function addRedClass() {
  header.classList.add('red');
}

// Add a click event listener to the 'red_header' element
redHeader.addEventListener('click', addRedClass);
