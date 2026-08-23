let choice = prompt(
    "1. Celsius to Fahrenheit\n" +
    "2. Fahrenheit to Celsius\n" +
    "3. Celsius to Kelvin\n" +
    "4. Kelvin to Celsius"
);

let temp = Number(prompt("Enter temperature:"));
let result;

if (choice == 1) {
    result = (temp * 9 / 5) + 32;
    console.log(temp + "°C = " + result.toFixed(2) + "°F");
}
else if (choice == 2) {
    result = (temp - 32) * 5 / 9;
    console.log(temp + "°F = " + result.toFixed(2) + "°C");
}
else if (choice == 3) {
    result = temp + 273.15;
    console.log(temp + "°C = " + result.toFixed(2) + " K");
}
else if (choice == 4) {
    result = temp - 273.15;
    console.log(temp + " K = " + result.toFixed(2) + "°C");
}
else {
    console.log("Invalid choice");
}