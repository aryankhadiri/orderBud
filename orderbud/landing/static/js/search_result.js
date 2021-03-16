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
    for (i = foodsDisplayed; i < foodsDisplayed + limitToShowFood; i++){
        food = food_data[i];
        $(".foods-results").append("<div class = 'food-div'><div class = 'left-picture-food'>"+ "<img></div>" + 
        "<div class = 'right-side-food'>"+"<div class = 'food-name'>" + food["_source"].name + 
        "</div><div class = 'food-rating'>"+ food["_source"].overal_rate +
        "</div><div class = 'food-description'>" + food["_source"].description + "</div>" +
        "<div class = 'by_restaurant'>" + "By: <a href = '/restaurants/"+food["_source"].restaurantId + "' class = 'restaurant-name-for-food'>"+food["_source"].restaurantName + "</a></div>" + "</div></div>");
    }
    foodsDisplayed += limitToShowFood;
}
function displayRestaurants(restaurants_data){
    if (Object.keys(restaurants_data).length - restaurantsDisplayed > limitPerItems){
        var limitToShowRest = limitPerItems;
    }
    else{
        var limitToShowRest = Object.keys(restaurants_data).length - restaurantsDisplayed;
    }
    for (i = restaurantsDisplayed; i < restaurantsDisplayed + limitToShowRest; i++){
        rest = restaurants_data[i]
        $(".restaurants-results").append("<div class = 'rest-div'><div class = 'left-picture-rest'>"+"<img></div>"+
        "<div class = 'right-side-rest'>"+"<div class = 'rest-name'>"+ rest["_source"].name + 
        "</div><div class = 'rest-rating'>" + rest["_source"].overal_rate + 
        "</div><div class = 'rest-address'>" + rest["_source"].city + ","  + rest["_source"].state + "</div></div>");
        
    }
}
$(document).ready(function(){
    var food_data = JSON.parse($("#foods_data").text());
    var restaurants_data = JSON.parse($("#restaurants_data").text());
    displayFoods(food_data);
    displayRestaurants(restaurants_data);
})
