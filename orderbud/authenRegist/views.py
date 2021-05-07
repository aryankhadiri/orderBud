from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import registerForm, LoginForm
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from elasticsearch import Elasticsearch, ElasticsearchException
from orderbud.settings import ELASTICSEARCH_HOST, ELASTICSEARCH_PORT
from datetime import datetime
from django.template.defaulttags import register
from details.views import getLatestId

# Create your views here.
def login_view(request):
    print(list(messages.get_messages(request)))

    if request.method == "POST":
        email = request.POST.get("Email-text")
        password = request.POST.get("password-text")
        user = authenticate(request, username = email, password = password)
        if user is not None:
            login(request, user)
        else:
            messages.add_message(request, messages.ERROR, "Invalid Email/Password")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    


    form = LoginForm()
    context = {
        "form":form
    }
    
    return render (request, "login.html", context)

def register_view(request):
    print(list(messages.get_messages(request)))
    #TODO register view
    if request.method == "POST":
        form2 = registerForm(request.POST, request.FILES)
        if form2.is_valid():
            user = form2.save()
            success_message = "User profile has been saved successfully."
            messages.add_message(request, messages.SUCCESS, success_message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))    
        else:
            for error in form2.errors:
                messages.add_message(request,messages.ERROR,form2.errors[error])

    form = registerForm()
    context = {
        "form": form
    }

    return render (request, "register.html", context)
@login_required
def messages_view(request, id):
    es = Elasticsearch([{'host': ELASTICSEARCH_HOST, 'port':ELASTICSEARCH_PORT}])

    if request.method == "POST":
        print(request.POST)
        sendByUser = "True"
        restaurantId = request.POST.get("restaurantId")
        userId = id
        messageText = request.POST.get("new-message")
        restaurantName = request.POST.get("restaurantName")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        latestId = getLatestId(es, "messages")
        newId = latestId + 1
        newMessage = {
            "id": newId, 
            "userId": userId, 
            "restaurantId":int(restaurantId), 
            "restaurantName":restaurantName, 
            "sendByUser":sendByUser, 
            "timestamp":timestamp, 
            "messageText":messageText}
        try:
            responseCreate = es.create(index = "messages", id = newId, body = newMessage)
        except ElasticsearchException as e:
            messages.add_message(request, messages.ERROR, "There was an error sending your message.")
            return redirect("/details/restaurants/{}".format(id))
    messages_list = getMessagesOfUser(id, es)
    if messages_list == -1:
        messages.add_message(messages.ERROR, "There was an error retrieving the messages.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))   
    messages_list_data = [x["_source"] for x in messages_list]
    messages_front = {}
    for m in messages_list_data:
        theDate = datetime.strptime(m["timestamp"],"%Y-%m-%d %H:%M:%S")
        newDate = theDate.strftime("%Y-%m-%d")
        time = theDate.strftime("%H:%M")
        m["timestamp"] = time
        if messages_front.get(m["restaurantName"]) == None:
            messages_front[m["restaurantName"]] = {newDate:[m]}
        else:
            if messages_front[m["restaurantName"]].get(newDate) == None:
                messages_front[m["restaurantName"]][newDate] = [m]
            else:
                messages_front[m["restaurantName"]].get(newDate).append(m)
    context = {
        "messages_list":messages_front
    }

    return render (request, "messages.html", context)

def send_message_view(request, userId, restId):
    es = Elasticsearch([{'host': ELASTICSEARCH_HOST, 'port':ELASTICSEARCH_PORT}])
    restaurant_info = es.get(index="restaurants", id=restId)
    restaurantName = restaurant_info["_source"]["name"]
    if request.method == "POST":
        messageText = request.POST.get("messageText")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        latestId = getLatestId(es, "messages")
        newId = latestId + 1
        newMessage = {
            "id": newId, 
            "userId": userId, 
            "restaurantId":restId, 
            "restaurantName":restaurantName, 
            "sendByUser":"True", 
            "timestamp":timestamp, 
            "messageText":messageText
            }
        try:
            responseCreate = es.create(index = "messages", id = newId, body = newMessage)
            messages.add_message(request, messages.SUCCESS, "Message sent successfully.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))   
        except ElasticsearchException as e:
            messages.add_message(request, messages.ERROR, "There was an error adding your review.")
            return redirect("/sendmessage/{}&{}".format(userId, restId))
    context = {
        "restName":restaurantName
    }
    return render(request, "sendMessage.html", context)

def logout_view(request):
    if request.method=='POST':
        logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))    

def getMessagesOfUser(id, es):
    search_body = {
        "sort":[
            {"timestamp":{
                "order":"asc"
            }}
        ],
        "query":{
            "match":{
                "userId":id
            }

        }
    }
    try:
        response = es.search(index = "messages", body= search_body, size=10000 )
    except ElasticsearchException as e:
        return -1   
    return response['hits']['hits']

    
@register.filter
def getFirstMessage(dictionary):
    message_list = list(dictionary.items())
    lastDateMessage = message_list[len(message_list) - 1]
    messagesOfLastDate = len(lastDateMessage[1])
    lastMessageDict = lastDateMessage[1][messagesOfLastDate-1]
    return lastMessageDict["messageText"]