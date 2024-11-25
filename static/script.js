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
