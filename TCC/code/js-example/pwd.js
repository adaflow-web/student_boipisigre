// This function takes a boolean parameter
// that says if password was entered correctly
// (true = yes, false = no)
function logIn(passwordIsCorrect) {
  if (passwordIsCorrect != true) {
    console.log("Your password is not correct, you can't log in");
  }
  else {
    console.log("Welcome back! You are now signed in.");
  }
}

// pas de vérification ....
