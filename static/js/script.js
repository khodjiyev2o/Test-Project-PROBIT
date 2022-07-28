

const checkBoxesForTime = document.querySelectorAll(".pick-time");

const timeValues = document.querySelectorAll(".time");

checkBoxesForTime.forEach((current, index) => {
  current.addEventListener("change", (e) => {
    timeValues[index].classList.remove("active");
    console.log('remove  class');
    if (e.target.checked) {
      timeValues[index].classList.add("active");
      console.log('add class');
    }
  });
});




const checkBoxesForDistance = document.querySelectorAll(".pick");

const DistanceValues = document.querySelectorAll(".distance");

checkBoxesForDistance.forEach((current, index) => {
  current.addEventListener("change", (e) => {
    DistanceValues[index].classList.remove("active");
    console.log('remove  class');
    if (e.target.checked) {
      DistanceValues[index].classList.add("active");
      console.log('add class');
    }
  });
});


