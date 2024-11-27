// Save scroll position in local storage before the page unloads#######################################################################
window.addEventListener("beforeunload", function () {
  localStorage.setItem("scrollPosition", window.scrollY);
});

// Function to smoothly scroll to a position   
function smoothScrollTo(targetY) {
  const startY = window.scrollY;
  const distance = targetY - startY;
  const duration = 300; // duration of the scroll (in milliseconds)
  let startTime = null;

  // Easing function (ease-in-out)
  function easing(t) {
    return t < 0.5
      ? 2 * t * t
      : (t - 1) * (2 * t - 2) + 1;
  }

  // Scroll animation function
  function animateScroll(timestamp) {
    if (!startTime) startTime = timestamp;
    const elapsedTime = timestamp - startTime;
    const progress = Math.min(elapsedTime / duration, 1);
    const easingProgress = easing(progress);

    // Calculate the new scroll position based on the easing function
    window.scrollTo(0, startY + distance * easingProgress);

    if (elapsedTime < duration) {
      requestAnimationFrame(animateScroll); // Continue the animation
    }
  }

  requestAnimationFrame(animateScroll); // Start the animation
}

// Restore scroll position after the page loads with custom smooth scroll
window.addEventListener("load", function () {
  setTimeout(function () { // Delay the scroll restoration to allow full rendering
    const scrollPosition = localStorage.getItem("scrollPosition");
    if (scrollPosition) {
      smoothScrollTo(parseInt(scrollPosition, 10)); // Smooth scroll to the saved position
      localStorage.removeItem("scrollPosition"); // Clear stored value after restoration
    }
  }, 200); // Use a small delay of 0 ms to allow the page to fully load
});

// Prevent page reload/jump after button submit or form submit
const form = document.querySelector('form'); // Assuming you are using a form to submit
if (form) {
  form.addEventListener('submit', function (event) {
    // Save the scroll position before submitting the form
    localStorage.setItem("scrollPosition", window.scrollY);
    // Prevent default form submission to avoid page reload
    event.preventDefault();

    // Optionally, you can perform some AJAX call here or manually submit the form after restoring scroll position.
    setTimeout(function () {
      form.submit(); // You can submit the form after the scroll position is saved
    }, 10); // Optional delay before submitting (to ensure scroll position is saved)
  });
}
// ############################################################################





















document.addEventListener("DOMContentLoaded", function () {
  const sliders = document.querySelectorAll(".range-slider");

  sliders.forEach(slider => {
    const range = slider.querySelector(".range-slider__range");
    const value = slider.querySelector(".range-slider__value");

    // Initialize the value display
    value.textContent = range.value;

    // Update the value display on input
    range.addEventListener("input", function () {
      value.textContent = this.value;
    });
  });
});


// // Save scroll position in local storage before the page unloads
// window.addEventListener("beforeunload", function () {
//   localStorage.setItem("scrollPosition", window.scrollY);
// });

// // Restore scroll position after the page loads
// window.addEventListener("load", function () {
//   const scrollPosition = localStorage.getItem("scrollPosition");
//   if (scrollPosition) {
//     window.scrollTo(0, parseInt(scrollPosition, 10));
//     localStorage.removeItem("scrollPosition"); // Clear stored value after restoration
//   }
// });




document.querySelectorAll(".range-slider__range").forEach((slider) => {
  slider.addEventListener("input", function () {
    this.nextElementSibling.textContent = this.value;
  });
});


$(document).ready(function() {
  $('#myForm').on('submit', function(e) {
    e.preventDefault();  // Prevent the form from submitting normally

    // Collect form data
    var formData = $(this).serialize();

    $.ajax({
      type: 'POST',
      url: '/',
      data: formData,
      success: function(response) {
        // Update the page with the response (the predicted output)
        $('.predictedOutput').html(response);
      },
      error: function() {
        alert('There was an error processing your request');
      }
    });
  });
});
















