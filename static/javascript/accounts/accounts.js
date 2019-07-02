import $ from 'jquery'

$(document).ready(function(){
    $("p").addClass("form-group");
    $("input").addClass("form-control");
    $("form > ul").addClass("list-group");
    $("ul.list-group > li").addClass("list-group-item");
    $("div.fb-login-button").attr("onlogin", verifyLogin());
});

function verifyLogin() {
  FB.getLoginStatus(function(response) {
    console.log(response);
  });
}
