from django.shortcuts import render
from elasticsearch import Elasticsearch, ElasticsearchException
from orderbud.settings import ELASTICSEARCH_HOST, ELASTICSEARCH_PORT, BASE_DIR
import os
# Create your views here.
def restaurants_details_view(request, id =id):
    es = Elasticsearch([{'host': ELASTICSEARCH_HOST, 'port':ELASTICSEARCH_PORT}])
    esResponse = es.get(index = "restaurants", id = id)
    restaurant_info = esResponse["_source"]
    esfoodResponse = searchForFoods(str(id), es)
    categorized_foods = {}
    for food in esfoodResponse:
        category = food["_source"]["category"]
        if categorized_foods.get(category) == None:
            categorized_foods[category] = []
            
        categorized_foods[category].append(food["_source"])
    
    pictures_path = "media/restaurants_pictures/{}/".format(id)
    list_of_files = os.listdir(BASE_DIR.joinpath(pictures_path))
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
    pictures_path = "media/foods_pictures/{}/".format(id)
    list_of_files = os.listdir(BASE_DIR.joinpath(pictures_path))
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