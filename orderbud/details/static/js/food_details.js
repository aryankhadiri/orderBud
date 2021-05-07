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
    displayReviews(reviews);
    $(".more-reviews").on("click",function(){
        displayReviews(reviews);
    })
})