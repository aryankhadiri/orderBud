var limitPerReviews = 10;
var reviewsDisplayed = 0;
function displayReviews(reviews_data){
    if (Object.keys(reviews_data).length - reviewsDisplayed > limitPerReviews){
        var limitToShowReviews = limitPerReviews;
    }
    else{
        var limitToShowReviews = Object.keys(reviews_data).length - reviewsDisplayed;
    }
    if (limitToShowReviews == 0){
        $(".more-reviews").addClass("no-show");
    }
    else{
        for (i = reviewsDisplayed; i < reviewsDisplayed + limitToShowReviews; i++){
            review = reviews_data[i]["_source"];
            $(".reviews").append("<div class = 'review-div'><div class = 'left-review-section'>"+
            "<div class = 'review-user'><div class = 'review-user-username'>"+review["reviewerName"]+"</div>"+
            "<div class = 'review-rate'>"+review["rate"]+"<img src='/media/icons/star.svg' class='star-icon'>"+"</div><div class = 'review-date'>"+review["timestamp"]+"</div>"+
            "</div></div>"+"<div class = 'right-review-section'><div class = 'review-title'>"+review["reviewTitle"]+
            "</div><div class = 'review-text'>"+review["reviewText"]+"</div>"+
            "</div>"+"</div>")
        }
        reviewsDisplayed += limitToShowReviews;
    }
}
$(document).ready(function(){
    $("#total-ratings").on("click", function(){
        document.getElementById("reviews").scrollIntoView({behavior: 'smooth'});
    })

    var reviews = JSON.parse($("#reviews_data").text());
    $(".filters div").on("click", function(){
        for (child of $(".filters").children()){
            child.classList.remove("active-filter");
        }
        if ($(this).text() == "Menu"){
            $(".restaurant_home").addClass("no-show");
            $(".menu-list").removeClass("no-show");
            $(this).addClass("active-filter");

        }
        if ($(this).text() == "Home"){
            $(".restaurant_home").removeClass("no-show");
            $(".menu-list").addClass("no-show");
            $(this).addClass("active-filter");
        }
    })
    /*var menu_data = JSON.parse($("#menu_data").text());
    for (category in menu_data){
        $(".menu-list").append("<div class = 'category div-" + category + "'></div>");
        for (food of menu_data[category]){
            $(".div-"+category).append("<div class = 'menu-item'>" + 
            "</div>");
        }
    }*/
    displayReviews(reviews);
    $(".more-reviews").on("click",function(){
        displayReviews(reviews);
    })
})
