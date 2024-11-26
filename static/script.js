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



// Assuming the form has input fields with IDs "name" and "email"
// const carcompany = document.getElementById("carcompany");
// const fueltype = document.getElementById("fueltype");
// const sellertype = document.getElementById("sellertype");
// const transmissiontype = document.getElementById("transmissiontype");
// const carowner = document.getElementById("carowner");
// const manufacturedyear = document.getElementById("manufacturedyear");
// const kmsdriven = document.getElementById("kmsdriven");
// const carmileage = document.getElementById("carmileage");
// const carenginecc = document.getElementById("carenginecc");
// const noofseats = document.getElementById("noofseats");


  document.getElementById("myForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission behavior 1 

    // Get the form values
    const carcompany = document.getElementById("carcompany").value;

    // Retain the values in the form fields
    document.getElementById("carcompany").value = carcompany;

    // You can add more form fields and their retention logic here
  });