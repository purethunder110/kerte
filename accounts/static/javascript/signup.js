
document.getElementById("Registeruser").addEventListener("click", function(){
  //age calculations
  var dobinput = new Date(document.getElementById("DOB").value);
  var today=new Date();
  var age = today.getFullYear() - dobinput.getFullYear();
  var monthDiff = today.getMonth() - dobinput.getMonth();

  if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < dobinput.getDate())) {
    age--;
  }
  console.log(age)
  //validating the age is even their
  if(isNaN(age)){
    const errorMessageElement = document.getElementById('errorMessage');
    errorMessageElement.textContent = "Please Enter Your DOB ";
    errorMessageElement.style.display = 'block';
    return;
  }

  data=new FormData();
  password=document.getElementById("Password").value
  cpassword=document.getElementById("CPassword").value

  let profile_pic=document.getElementById('profile_pic');
  let profile=profile_pic.files[0]
  //check if the file is image or not
  if (profile==undefined || !profile.type.match('image.*')){
    alert("image not selected")
  }
  else{
    data.append("profile_pic",profile)
  }


  
  if (password===cpassword){
    data.append("Age",age)
    data.append("SignupDetails","true")
    data.append("csrfmiddlewaretoken",document.getElementById("csrf_token").value)
    data.append("first_name",document.getElementById("first_name").value);
    data.append("last_name",document.getElementById("last_name").value);
    data.append("username",document.getElementById("Username").value);
    data.append("password",document.getElementById("Password").value);
    data.append("email",document.getElementById("email").value);

    axios.post('',data)
    .then(res=>{
      const successMessageElement = document.getElementById('successMessage');
      successMessageElement.textContent = 'Registered successfullly.';
      successMessageElement.style.display = 'block';
    })
    .catch(error=>{
      errorhandlefunc(error.response.status,error.response.data.error)
  });
  }
  else{
    const errorMessageElement = document.getElementById('errorMessage');
    errorMessageElement.textContent = 'Password and Confirm Password does not match';
    errorMessageElement.style.display = 'block';
  }

});


function errorhandlefunc(status_code,error_message){
    const errorMessageElement = document.getElementById('errorMessage');
    
    if (status_code==406){
      errorMessageElement.textContent = error_message;
    }
    else{
      errorMessageElement.textContent = 'An error occurred. Please try again later.';
    }
    
    errorMessageElement.style.display = 'block';
}
window.onload = function () {
  document.getElementById('DOB').setAttribute('max', new Date(new Date().getFullYear() - 16, new Date().getMonth(), new Date().getDate()).toISOString().split('T')[0]);
}