import $ from 'jquery'


document.addEventListener("facebookLoaded", function(){
    verifyLogin();
});



function verifyLogin() {
  FB.getLoginStatus(function(response) {
    console.log(response);
  });
}
