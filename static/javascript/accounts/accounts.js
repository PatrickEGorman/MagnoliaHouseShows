import $ from 'jquery'

$(document).ready(function(){
    $("p").addClass("form-group");
    $("input").addClass("form-control");
    $("form > ul").addClass("list-group");
    $("ul.list-group > li").addClass("list-group-item");
    $("div.fb-login-button").attr("onlogin", postLogin());
});

function postLogin() {
  FB.getLoginStatus(function(response) {
      if(response.status==="connected"){
          fb.api('/me', function(response){
              console.log(response);
          })
        // var csrftoken = Cookies.get('csrftoken');
        // $.ajaxSetup({
        //     beforeSend: function(xhr, settings) {
        //         if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        //             xhr.setRequestHeader("X-CSRFToken", csrftoken);
        //         }
        //     }
        // });
        // $,post("/users/authenticate_facebook")
      });
    }
}
