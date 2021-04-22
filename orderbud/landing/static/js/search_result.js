var limitPerItems = 10;
var foodsDisplayed = 0;
var restaurantsDisplayed = 0;
function displayFoods(food_data){
    if (Object.keys(food_data).length-foodsDisplayed > limitPerItems){
        var limitToShowFood = limitPerItems;
    }
    else{
        var limitToShowFood = Object.keys(food_data).length-foodsDisplayed;
    }
    if (limitToShowFood == 0){
        $("#more-food-button").addClass("no-show");
    }
    else{

        for (i = foodsDisplayed; i < foodsDisplayed + limitToShowFood; i++){
            food = food_data[i];
            $(".foods-results").append("<div class = 'food-div'><div class = 'left-picture-food'>"+ "<img></div>" + 
            "<div class = 'right-side-food'>"+"<div class = 'food-name'>" + "<a href = '/details/foods/" + food["_source"]["id"] + "'>"+ food["_source"].name + 
            "</a></div><div class = 'food-rating'>"+ "<div class = 'rate-value'>" + food["_source"].overal_rate +
            "</div><div class = 'star-rate'><img src = '/media/icons/star.svg' class = 'star-icon'></div>"+
            "<div class = 'total-rate'>" + "("+ food["_source"].ratings + ")" + "</div></div>" + "<div class = 'food-description'>" + food["_source"].description + "</div>" +
            "<div class = 'by-restaurant'>" + "By: <a href = '/details/restaurants/"+food["_source"].restaurantId + "' class = 'restaurant-name-for-food'>"+food["_source"].restaurantName + "</a></div>" + "</div></div>");
        }
        foodsDisplayed += limitToShowFood;
    }
}
function displayRestaurants(restaurants_data){
    if (Object.keys(restaurants_data).length - restaurantsDisplayed > limitPerItems){
        var limitToShowRest = limitPerItems;
    }
    else{
        var limitToShowRest = Object.keys(restaurants_data).length - restaurantsDisplayed;
    }
    if (limitToShowRest == 0){
        $("#more-restaurant-button").addClass("no-show");
    }
    else{
        for (i = restaurantsDisplayed; i < restaurantsDisplayed + limitToShowRest; i++){
            rest = restaurants_data[i]
            $(".restaurants-results").append("<div class = 'rest-div'><div class = 'left-picture-rest'>"+"<img src = '/media/"+rest["_source"].main_picture +"'></div>"+
            "<div class = 'right-side-rest'>"+"<div class = 'rest-name'>"+ "<a href = '/details/restaurants/"+rest["_source"]["id"] + "'>" + rest["_source"].name + "</a>" +
            "</div><div class = 'rest-rating'>" + "<div class = 'rate-value'>" + rest["_source"].overal_rate + 
            "</div><div class = 'star-rate'><img src = '/media/icons/star.svg' class = 'star-icon'></div>"+ "<div class = 'total-rate'>" + "(" + rest["_source"].ratings + ")" + "</div>" +
            "</div><div class = 'rest-address'>" + rest["_source"].city + ","  + rest["_source"].state + "</div></div>");
        }
        restaurantsDisplayed += limitToShowRest;
    }
}
$(document).ready(function(){
    var foods_data = JSON.parse($("#foods_data").text());
    var restaurants_data = JSON.parse($("#restaurants_data").text());
    displayFoods(foods_data);
    displayRestaurants(restaurants_data);
    $(".filters div").on("click", function(){
        for (child of $(".filters").children()){
            if (child.classList.contains("active-filter")){
                child.classList.remove("active-filter");

            }
        }
            
        $(this).addClass("active-filter");
        let text = $(this).text();
        switch (text){
            case "Foods":
                //$(".restaurant-title").remove();
                //$(".restaurants-results").empty();
                //$(".foods-results").empty();
                //foodsDisplayed = 0;
                //displayFoods(food_data);
                $(".food-title").removeClass("no-show");
                $(".foods-results").removeClass("no-show");
                $("#more-food-button").removeClass("no-show");
                $(".restaurant-title").addClass("no-show");
                $(".restaurants-results").addClass("no-show");
                $("#more-restaurant-button").addClass("no-show");
                

                break;
            case "Restaurants":
                $(".food-title").addClass("no-show");
                $(".foods-results").addClass("no-show");
                $(".restaurant-title").removeClass("no-show");
                $(".restaurants-results").removeClass("no-show");
                $("#more-food-button").addClass("no-show");
                $("#more-restaurant-button").removeClass("no-show");


                break;
            default:
                $(".restaurant-title").removeClass("no-show");
                $(".restaurants-results").removeClass("no-show");
                $(".food-title").removeClass("no-show");
                $(".foods-results").removeClass("no-show");
                $("#more-food-button").removeClass("no-show");
                $("#more-restaurant-button").removeClass("no-show");


        }
    })
    $("#more-restaurant-button").on("click",function(){
        displayRestaurants(restaurants_data);
    })
    $("#more-food-button").on("click",function(){
        displayFoods(foods_data);
    })

})
