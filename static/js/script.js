const prices = document.querySelectorAll(".price");

prices.forEach((price) => {
  price.addEventListener("click", () => {
    let activePrice = document.querySelector(".col-4.price.active");

    activePrice.className = activePrice.className.replace(" active", "");

    price.classList.add("active");
  });
});

const distanceValues = document.querySelectorAll(".distance");

const checkBoxesForDistance = document.querySelectorAll(".pick");

checkBoxesForDistance.forEach((current, index) => {
  current.addEventListener("change", () => {
    let activeDistance = document.querySelector(".distance.active");

    activeDistance.className = activeDistance.className.replace(" active", "");

    distanceValues[index].classList.add("active");
  });
});

const checkBoxesForTime = document.querySelectorAll(".pick-time");

const timeValues = document.querySelectorAll(".time");

checkBoxesForTime.forEach((current, index) => {
  current.addEventListener("change", () => {
    let activeTimeValue = document.querySelector(".time.active");

    activeTimeValue.className = activeTimeValue.className.replace(
      " active",
      ""
    );
    timeValues[index].classList.add("active");
  });
});

const starsFirstRow = document.querySelectorAll(".star-1");

starsFirstRow.forEach((current, index, array) => {
  current.addEventListener("click", () => {
    for (let i = 0; i <= index; i++) {
      array[i].classList.add("checked");
    }
  });
});

const starsSecondRow = document.querySelectorAll(".star-2");

starsSecondRow.forEach((current, index, array) => {
  current.addEventListener("click", () => {
    for (let i = 0; i <= index; i++) {
      array[i].classList.add("checked");
    }
  });
});
