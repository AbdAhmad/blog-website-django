function signupPasswordOneVisibilityToggle() {
    let passwordOne = document.getElementById("passwordOne");
        if (passwordOne.type === "password") {
            passwordOne.type = "text";
        } else {
            passwordOne.type = "password";
        }
    }

function signupPasswordTwoVisibilityToggle() {
    let passwordTwo = document.getElementById("passwordTwo");
    if (passwordTwo.type === "password") {
        passwordTwo.type = "text";
    } else {
        passwordTwo.type = "password";
    }
}

function loginPasswordVisibilityToggle() {
    let myInput = document.getElementById("myInput");
        if (myInput.type === "password") {
            myInput.type = "text";
        } else {
            myInput.type = "password";
        }
}