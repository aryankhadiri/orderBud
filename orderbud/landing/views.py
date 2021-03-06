from django.shortcuts import render, redirect
from elasticsearch import Elasticsearch
from orderbud.settings import ELASTICSEARCH_HOST, ELASTICSEARCH_PORT
# Create your views here.
def landing_view(request):

    result = searchForFood("chicken",es)
    context = {'name':"Ayush"}
    print(result)
    return render(request, "landing.html", context)
def search_result_view(request):

    search_term = request.GET.get("search-field")
    if search_term == "" or search_term is None:
        return redirect("landing_view")
    
    es = Elasticsearch([{'host': ELASTICSEARCH_HOST, 'port':ELASTICSEARCH_PORT}])
    foods = searchForFood(search_term,es)
    restaurants = searchForRestaurant(search_term, es)
    food_total = len(foods)
    restaurants_total = len(restaurants)
    if foods != 0 or restaurants != 0:
        #TODO no result found
        total_result = 0
    elif foods != -1 or restaurants != -1:
        #TODO there was an error getting the information you want
        total_result = None

    total_result = food_total + restaurants_total

    context = {}
    return render(request, "search_result.html", context)


########################  Helper Functions ####################
def searchForFood(searchTerm, es):
    searchBody = {
        "query":{
            "query_string":{
                "query":searchTerm
            }
        }
    }
    try:
        search_result = es.search(index="foods", body = searchBody, size=1000)
    except ElasticsearchException:
        return -1
    total_hit = search_result["hits"]["total"]["value"]
    if total_hit == 0:
        return 0
    return search_result["hits"]["hits"]

def searchForRestaurant(searchTerm, es):
    searchBody = {
        "query": {
            "query_string": {
            "query": searchTerm
            }
        }
    }
    try:
        search_result = es.search(index="restaurants", body = searchBody, size=1000)
    except ElasticsearchException:
        return -1
    print(search_result)
    total_hit = search_result["hits"]["total"]["value"]
    if total_hit == 0:
        return 0
    return search_result["hits"]["hits"]