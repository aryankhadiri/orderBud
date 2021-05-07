$(document).ready(function(){
    $(".login").on("click", function(){
        $(".login-dropdown-menu").slideToggle("slow");
        document.getElementById("login-nav-button").scrollIntoView({behavior: 'slow'});
    })
});