const form = document.querySelector("form");
otpField = form.querySelector(".password"),
otpInput = otpField.querySelector("input");

form.onsubmit = (e) => {
    e.preventDefault();
    console.log(otpInput.value);
}
