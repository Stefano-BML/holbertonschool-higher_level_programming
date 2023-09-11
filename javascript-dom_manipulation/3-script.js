// Get the elements with id 'toggle_header' and the header element
var toggleHeader = document.getElementById('toggle_header');
var header = document.querySelector('header');

// Function to toggle the class of the header element
function toggleHeaderClass() {
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else if (header.classList.contains('green')) {
    header.classList.remove('green');
    header.classList.add('red');
  }
}

// Add a click event listener to the 'toggle_header' element
toggleHeader.addEventListener('click', toggleHeaderClass);
