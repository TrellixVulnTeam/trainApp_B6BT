// First Reveal Password Function
function passReveal1() {
  var pwd1 = document.getElementById("pwd1");
  var eye1 = document.getElementById("eye1");

  // Change color of eye element

  if (eye1.classList.contains('fa-eye')) {
      eye1.classList.remove("fa-eye");
      eye1.classList.add("fa-eye-slash");
  }
 else {
      eye1.classList.remove("fa-eye-slash");
      eye1.classList.add("fa-eye");
}

  // Make password visible
  (pwd1.type == 'password') ? pwd1.type = 'text' :
  pwd1.type = 'password'

};

function passReveal2() {
  var pwd2 = document.getElementById("pwd2");
  var eye2 = document.getElementById("eye2");

  // Change color of eye element
  if (eye2.classList.contains('fa-eye')) {
      eye2.classList.remove("fa-eye");
      eye2.classList.add("fa-eye-slash");
  }
 else {
      eye2.classList.remove("fa-eye-slash");
      eye2.classList.add("fa-eye");
}

  // Make password visible
  (pwd2.type == 'password') ? pwd2.type = 'text' :
  pwd2.type = 'password'

};