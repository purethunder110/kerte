const form = document.querySelector("form");
eField = form.querySelector(".email"),
eInput = eField.querySelector("input"),
pField = form.querySelector(".password"),
pInput = pField.querySelector("input");

form.onsubmit = (e) => {
    const sendform=new FormData() 
    e.preventDefault();

    (eInput.value == "") ? eField.classList.add("shake", "error"): checkEmail();
    (pInput.value == "") ? pField.classList.add("shake", "error"): checkPass();

    setTimeout(() => {
        eField.classList.remove("shake");
        pField.classList.remove("shake");
    }, 500);

    eInput.onkeyup = () => { checkEmail(); }
    pInput.onkeyup = () => { checkPass(); }

    function checkEmail() {
        let pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
        if (!eInput.value.match(pattern)) {
            eField.classList.add("error");
            eField.classList.remove("valid");
            let errorTxt = eField.querySelector(".error-txt");

            (eInput.value != "") ? errorTxt.innerText = "Enter a valid email address": errorTxt.innerText = "Email can't be blank";
        } else {
            eField.classList.remove("error");
            eField.classList.add("valid");
        }
    }

    function checkPass() {
        if (pInput.value == "") {
            pField.classList.add("error");
            pField.classList.remove("valid");
        } else {
            pField.classList.remove("error");
            pField.classList.add("valid");
        }
    }

    if (!eField.classList.contains("error") && !pField.classList.contains("error")) {
        const typing= validateLoginAndPassword(eInput.value,pInput.value)
        ID=document.getElementById("LoginID").value;
        password=document.getElementById("LoginPassword").value;
        csrftoken=document.getElementById("csrfmiddlewaretoken").value;
        sendform.append("csrfmiddlewaretoken",csrftoken)
        sendform.append(typing,ID)
        sendform.append("password",password)

        console.log(eInput.value,pInput.value)
        console.log(typing)

    }
}


function validateLoginAndPassword(login, password) {
    // Regular expression for username with at least 6 characters and 2 numbers
    const usernameRegex = /^(?=.*[A-Za-z])(?=.*\d.*\d)[A-Za-z\d]{6,}$/;
    
    // Regular expression for validating email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    
    // Regular expression for password between 8 and 16 characters with at least one uppercase, one lowercase, one number, and one special character
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+={}\[\]:;'"<>,.?/\\-])[A-Za-z\d!@#$%^&*()_+={}\[\]:;'"<>,.?/\\-]{8,16}$/;

    // Check if the login is a valid username or email
    if (passwordRegex.test(password)) {
        if (emailRegex.test(login)){
            return "Email"
        }else if (usernameRegex.test(login)){
            return "username"
        }
    } else {
        return "invalid"; // Login or password do not meet the criteria
    }
}
/*
function checksandvalidations(){
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const usernameRegex = /^(?=.*[A-Za-z])(?=.*\d.*\d)[A-Za-z\d]{6,}$/;
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+={}\[\]:;'"<>,.?/\\-])[A-Za-z\d!@#$%^&*()_+={}\[\]:;'"<>,.?/\\-]{8,16}$/;

}

document.getElementById("submitbutton").addEventListener("click",function(e){
    e.preventDefault();
    //element data
    ID=document.getElementById("LoginID");
    password=document.getElementById("LoginPassword");
    csrftoken=document.getElementById("csrfmiddlewaretoken").value;
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const usernameRegex = /^(?=.*[A-Za-z])(?=.*\d.*\d)[A-Za-z\d]{6,}$/;
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+={}\[\]:;'"<>,.?/\\-])[A-Za-z\d!@#$%^&*()_+={}\[\]:;'"<>,.?/\\-]{8,16}$/;
    if(ID.value==""){
        (eInput.value == "") ? eField.classList.add("shake", "error"): checkEmail();
    }
    function checkEmail(){
        console.log("the mail works??");
    }
    setTimeout(() => {
        eField.classList.remove("shake");
        pField.classList.remove("shake");
    }, 500);

    eInput.onkeyup = () => {  }
    pInput.onkeyup = () => {  }
    const formsend =new FormData()

});
*/