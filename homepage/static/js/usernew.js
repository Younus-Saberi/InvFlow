// function for validation of register form
function validateRegister() {

    var username = document.getElementById("register-name").value;
    var useremail = document.getElementById("register-email").value;
    var password = document.getElementById("register-password").value;
    var repassword = document.getElementById("register-repassword").value;

    //validation for registration form from above code
    if(username=="" || useremail=="" || password=="" || repassword==""){
      alert("All fields are required");
      return false;
    }
    else if(password.length < 6){
      alert("Password must be at least 6 characters long.");
      return false;
    }
    else if(password != repassword){
      alert("Password and Confirm Password must be same.");
      return false;
    }
    else{
      // if all the validation is passed then redirect to the home page
      // window.location.replace('http://localhost:8000');
      alert("Your details are saved successfully")
      return true;
    }
    }


  // function for validation of login form
  function validateLoginForm() {
    // alert("Login Button was clicked on login form");

    var useremail = document.getElementById("login-email").value;
    var password = document.getElementById("login-password").value;
    
    //validation for login form from above code
    if(useremail=="" || password==""){
        alert("All fields are required");
        return false;
    }
    else if(password.length < 6){
        alert("Password must be at least 6 characters long.");
        return false;
    }
    else{

        // if all the validation is passed then redirect to the home page
        window.location.replace('http://localhost:8000');
        alert("You are logged in successfully")
        return true;
    }
    }   