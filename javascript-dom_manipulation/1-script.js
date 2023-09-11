// Get the element with id 'red_header'
var redHeader = document.getElementById('red_header');

// Function to change the header text color to red when clicked
function HeaderColor() {
  var header = document.querySelector('header');
  header.style.color = '#FF0000';
}

// Add a click event listener to the 'red_header' element
redHeader.addEventListener('click', HeaderColor);
