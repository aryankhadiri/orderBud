from django.shortcuts import render, redirect
from elasticsearch import Elasticsearch, ElasticsearchException
from orderbud.settings import ELASTICSEARCH_HOST, ELASTICSEARCH_PORT, BASE_DIR
import os
from datetime import datetime
from django.contrib import messages

# Create your views here.
def restaurants_details_view(request, id =id):
    es = Elasticsearch([{'host': ELASTICSEARCH_HOST, 'port':ELASTICSEARCH_PORT}])
    esResponse = es.get(index = "restaurants", id = id)
    restaurant_info = esResponse["_source"]
    esfoodResponse = searchForFoods(str(id), es)
    if request.method == "POST":
        print(request.POST)
        #when review gets submitted
        reviewText = request.POST.get("reviewText")
        reviewTitle = request.POST.get("reviewTitle")
        rateStr = request.POST.get("rating")
        rate = int(rateStr)
        reviewerName = request.user.username
        reviewerId = request.user.id
        latestId = getLatestId(es, "restaurant_reviews")
        
        newId = latestId+1
        nowDate = datetime.now().strftime("%Y-%m-%d")
        newReview = {
            "id":newId,
            "reviewerName":reviewerName,
            "reviewerId": reviewerId,
            "reviewText":reviewText,
            "reviewTitle":reviewTitle,
            "timestamp":nowDate,
            "rate":rate,
            "restaurant_id":id
        }
        try:
            responseCreate = es.create(index = "restaurant_reviews", id = newId, body = newReview)
            messages.add_message(request, messages.SUCCESS, "Review added successfully.")
        except ElasticsearchException as e:
            messages.add_message(request, messages.ERROR, "There was an error adding your review.")
            return redirect("/details/restaurants/{}".format(id))
        current_rate = restaurant_info["overall_rate"]
        allratings = restaurant_info["ratings"]
        newAllRatings = allratings + 1
        new_rate = round(((current_rate * allratings) + rate)/newAllRatings,1)
        update_body = {
            "doc":{
                "overall_rate":new_rate,
                "ratings": newAllRatings
            }
            
        }
        try:
            response = es.update("restaurants", body = update_body, id = id)
        except ElasticsearchException as e:
            messages.add_message(messages.ERROR, "There was an error updating the ratings.")
        return redirect("/details/restaurants/{}".format(id))
    
    categorized_foods = {}
    for food in esfoodResponse:
        category = food["_source"]["category"]
        if categorized_foods.get(category) == None:
            categorized_foods[category] = []
            
        categorized_foods[category].append(food["_source"])
    
    pictures_path = "media/restaurants_pictures/{}/".format(id)
    try:
        list_of_files = os.listdir(BASE_DIR.joinpath(pictures_path))
    except FileNotFoundError as e:
        list_of_files = []
    list_of_pictures_path = ["/"+pictures_path+path for path in list_of_files]
    reviews = searchReviews("restaurant_reviews", es, id)

    context = {
        "restaurant_info":restaurant_info,
        "pictures":list_of_pictures_path,
        "menu": categorized_foods,
        "reviews":reviews
    }
    return render(request, "restaurant_detail.html", context)

def foods_details_view(request, id = id):
    es = Elasticsearch([{'host': ELASTICSEARCH_HOST, 'port':ELASTICSEARCH_PORT}])
    esResponse = es.get(index = "foods", id = id)
    food_info = esResponse["_source"]
    if request.method == "POST":
        #when review gets submitted
        reviewText = request.POST.get("reviewText")
        reviewTitle = request.POST.get("reviewTitle")
        rateStr = request.POST.get("rating")
        rate = int(rateStr)
        reviewerName = request.user.username
        reviewerId = request.user.id
        latestId = getLatestId(es, "food_reviews")
        
        newId = latestId+1
        nowDate = datetime.now().strftime("%Y-%m-%d")
        newReview = {
            "id":newId,
            "reviewerName":reviewerName,
            "reviewerId": reviewerId,
            "reviewText":reviewText,
            "reviewTitle":reviewTitle,
            "timestamp":nowDate,
            "rate":rate,
            "food_id":id
        }
        try:
            responseCreate = es.create(index = "food_reviews", id = newId, body = newReview)
            messages.add_message(request, messages.SUCCESS, "Review added successfully.")
        except ElasticsearchException as e:
            messages.add_message(request, messages.ERROR, "There was an error adding your review.")
            return redirect("/details/foods/{}".format(id))
        current_rate = food_info["overall_rate"]
        allratings = food_info["ratings"]
        newAllRatings = allratings + 1
        new_rate = round(((current_rate * allratings) + rate)/newAllRatings,1)
        update_body = {
            "doc":{
                "overall_rate":new_rate,
                "ratings": newAllRatings
            }
            
        }
        try:
            response = es.update("foods", body = update_body, id = id)
        except ElasticsearchException as e:
            messages.add_message(messages.ERROR, "There was an error updating the ratings.")
        return redirect("/details/foods/{}".format(id))
    pictures_path = "media/food_pictures/{}/".format(id)
    try:
        list_of_files = os.listdir(BASE_DIR.joinpath(pictures_path))
    except FileNotFoundError as e:
        list_of_files = []
    list_of_pictures_path = ["/"+pictures_path+path for path in list_of_files]
    reviews = searchReviews("food_reviews", es, id)

    context = {
        "food_info":food_info,
        "pictures":list_of_pictures_path,
        "reviews":reviews

    }
    return render(request, "food_detail.html", context)

""" ------------------ Helper Function --------------"""
def searchForFoods(restaurant_id, es):
    search_body = {
        "query": {
            "match": {
                "restaurantId": restaurant_id
            }
        }
    }
    try:
        search_result = es.search(index="foods", body = search_body, size=1000)
    except ElasticsearchException:
        return -1
    total_hit = search_result["hits"]["total"]["value"]
    
    return search_result["hits"]["hits"]

def searchReviews(index, es, id):
    if index == "food_reviews":
        search_body = {
                "sort": [
                {
                    "timestamp": {
                        "order": "desc"
                    }
                }
                ], 
                "query":{
                    "match": {
                    "food_id": id
                    }
                }
            }
    elif index == "restaurant_reviews": 
        search_body = {
            "sort": [
            {
                "timestamp": {
                    "order": "desc"
                }
            }
            ], 
            "query":{
                "match": {
                "restaurant_id": id
                }
            }
        }
    try:
        search_result = es.search(index = index, body = search_body, size = 1000)
    except ElasticsearchException:
        return -1
    total_hit = search_result["hits"]["total"]["value"]
    
    return search_result["hits"]["hits"]

def getLatestId(es, index):
    search_body = {
        "sort":[{
            "id":{
                "order":"desc"
            }
        }]
        ,"query":{
            "match_all":{}
        }
    }
    try:
        response = es.search(index=index, body=search_body,size=1)
    except ElasticsearchException:
        return -1
    return response["hits"]["hits"][0]["_source"]["id"]