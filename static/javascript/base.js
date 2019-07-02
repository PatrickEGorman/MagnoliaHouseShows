import $ from 'jquery'


$.on("facebookLoaded"){
    verifyLogin();
}


function verifyLogin() {
  FB.getLoginStatus(function(response) {
    console.log(response);
  });
}
