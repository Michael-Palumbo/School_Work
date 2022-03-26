function checkForm() {
	console.log("Reached")
    var name = document.getElementById("fullName")
    name.style.border = "1px solid #aaa"
    var email = document.getElementById("email")
    email.style.border = "1px solid #aaa"
    var password = document.getElementById("password")
    password.style.border = "1px solid #aaa"
    var conPassword = document.getElementById("passwordConfirm")
    conPassword.style.border = "1px solid #aaa"

    var errorFound = false

    document.getElementById("formErrors").innerHTML = "<ul>"
    if (name.value < 1){
    	addError("Missing full name.")
    	name.style.border = "2px solid red"
    	errorFound = true
    }
    if (!/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,5}$/.test(email.value)){
    	addError("Invalid or missing email address.")
    	email.style.border = "2px solid red"
    	errorFound = true
    }
    if (!(password.value.length >= 10 && password.value.length <= 20)){
    	addError("Password must be between 10 and 20 characters.")
    	password.style.border = "2px solid red"
    	errorFound = true
    }
	if (!/[a-z]/.test(password.value)){
    	addError("Password must contain at least one lowercase character.")
    	password.style.border = "2px solid red"
    	errorFound = true
    }
    if (!/[A-Z]/.test(password.value)){
    	addError("Password must contain at least one uppercase character.")
    	password.style.border = "2px solid red"
    	errorFound = true
    }
    if (!/[0-9]/.test(password.value)){
    	addError("Password must contain at least one digit.")
    	password.style.border = "2px solid red"
    	errorFound = true
    }
    if (password.value != conPassword.value){
    	addError("Password and confirmation password don't match.")
    	password.style.border = "2px solid red"
    	errorFound = true
    }
    document.getElementById("formErrors").innerHTML += "</ul>"

    if (errorFound)
    	document.getElementById("formErrors").style.display = "block"
    else{
    	console.log("No Issues")
    	document.getElementById("formErrors").style.display = "none"
    	document.getElementById("formErrors").innerText = ""
    }
}

function addError(errorMessage){
	document.getElementById("formErrors").innerHTML += `<li> ${errorMessage} </li>`
}

document.getElementById("submit").addEventListener("click", function(event) {
   checkForm();

   // Prevent default form action. DO NOT REMOVE THIS LINE
   event.preventDefault();
});