from django.shortcuts import render
from elasticsearch import Elasticsearch
from orderbud.settings import ELASTICSEARCH_HOST, ELASTICSEARCH_PORT, BASE_DIR
import os
# Create your views here.
def restaurants_details_view(request, id =id):
    es = Elasticsearch([{'host': ELASTICSEARCH_HOST, 'port':ELASTICSEARCH_PORT}])
    esResponse = nt_info = es.get(index = "restaurants", id = id)
    restaurant_info = esResponse["_source"]
    
    pictures_path = "media/restaurants_pictures/{}/".format(id)
    list_of_files = os.listdir(BASE_DIR.joinpath(pictures_path))
    list_of_pictures_path = ["/"+pictures_path+path for path in list_of_files]
   
    context = {
        "restaurant_info":restaurant_info,
        "pictures":list_of_pictures_path
    }
    return render(request, "restaurant_detail.html", context)