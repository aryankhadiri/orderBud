$(document).ready(function(){
    $(".login").on("click", function(){
        $(".login-dropdown-menu").toggle();
        document.getElementById("login-nav-button").scrollIntoView({behavior: 'smooth'});
    })
});