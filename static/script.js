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


// Save scroll position in local storage before the page unloads
window.addEventListener("beforeunload", function () {
  localStorage.setItem("scrollPosition", window.scrollY);
});

// Restore scroll position after the page loads
window.addEventListener("load", function () {
  const scrollPosition = localStorage.getItem("scrollPosition");
  if (scrollPosition) {
    window.scrollTo(0, parseInt(scrollPosition, 10));
    localStorage.removeItem("scrollPosition"); // Clear stored value after restoration
  }
});