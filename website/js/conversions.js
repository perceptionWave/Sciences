// notes
// Online learning modules
// https://learn.microsoft.com/en-us/training/modules/get-started-with-web-development/7-summary 
"use strict";

// theme switcher
const switcher = document.querySelector(".btn");

switcher.addEventListener("click", function () {
  document.body.classList.toggle("light-theme");
  document.body.classList.toggle("dark-theme");

  const className = document.body.className;
  if (className == "light-theme") {
    this.textContent = "Dark";
  } else {
    this.textContent = "Light";
  }

  console.log("current class name: " + className);
});

// Unit measurment case
// function: switchUnitOfMeasurmentCase

function switch_unit_of_measurement() {
  var unit_of_measurement_list = document.getElementById("unit-of-measurement");
  var conversion_unit_input = document.getElementById("conversion-unit");

  switch (unit_of_measurement_list.value) {
    case "Length":
      conversion_unit_input.innerHTML =
        '<option value="ym">ym</option>< option value = "zm" > zm</option ><option value="at">at</option><option value="fm">fm</option><option value="pm">pm</option><option value="nm">nm</option><option value="um">um</option><option value="mm">mm</option><option value="cm">cm</option><option value="dm">dm</option><option value="m" selected>m</option><option value="dam">dam</option><option value="hm">hm</option><option value="km">km</option><option value="Mm">Mm</option><option value="Gm">Gm</option><option value="Tm">Tm</option><option value="Pm">Pm</option><option value="Em">Em</option><option value="Zm">Zm</option><option value="Ym">Ym</option><option value="pound">pound</option><option value="ounce">ounce</option><option value="carat">carat</option><option value="Short_ton">Short ton</option><option value="Long_ton">Long ton UK</option><option value="tonne">tonne</option>';
      break;
    case "Mass":
      conversion_unit_input.innerHTML =
        "<option value='a'>A</option><option value='b'>B</option><option value='c'>C</option>";
      break;
    case "Area":
      conversion_unit_input.innerHTML =
        "<option value='x'>X</option><option value='y'>Y</option><option value='z'>Z</option>";
      break;
    case "Volume":
      conversion_unit_input.innerHTML =
        "<option value='apple'>Apple</option><option value='banana'>Banana</option><option value='orange'>Orange</option>";
      break;
    default:
      conversion_unit_input.innerHTML =
        "<option value='default'>Please select an option from the first dropdown</option>";
  }
}

// https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/number#pattern_validation
const convert_input = () => {
  // read user input
  // let user_input = document.querySelector("conversion_input");
  //
  // output conversion output
};

// Map Data for units of conversion
// Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map
const length = new Map([
  ["m", 1],
  ["ym", m * Math.pow(10, 24)],
  ["zm", m * Math.pow(10, 21)],
  ["at", m * Math.pow(10, 18)],
  ["fm", m * Math.pow(10, 15)],
  ["pm", m * Math.pow(10, 12)],
  ["nm", m * Math.pow(10, 9)],
  ["um", m * Math.pow(10, 6)],
  ["mm", m * Math.pow(10, 3)],
  ["cm", m * Math.pow(10, 2)],
  ["dm", m * Math.pow(10, 1)],
  ["dam", m * Math.pow(10, -1)],
  ["hm", m * Math.pow(10, -2)],
  ["km", m * Math.pow(10, -3)],
  ["Mm", m * Math.pow(10, -6)],
  ["Gm", m * Math.pow(10, -9)],
  ["Tm", m * Math.pow(10, -11)],
  ["Pm", m * Math.pow(10, -15)],
  ["Em", m * Math.pow(10, -18)],
  ["Zm", m * Math.pow(10, -21)],
  ["Ym", m * Math.pow(10, -24)],
]);

// for (const [key, value] of length) {
//   console.log(`${key} goes ${value}`);
// }

function convert(input, from, to) {
  // this.input = input
  // this.from = from
  // this.to = to
  // bind from to selection list and to map
  // bind to to selection list and to map
  // convert using math
  // return output value
}
