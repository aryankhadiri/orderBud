var restaurantName;
var restaurantId;
var currentChat;
var messages;
$(document).ready(function(){
    messages = JSON.parse($("#list_messages").text());
    console.log(messages)
    console.log(messages);
    $(".chat").on("click", function(){
        currentChat = $(this);
        $(".sent-message").show();
        $(".messages-box").empty();
        $(".chat-list").find(".active-chat").removeClass("active-chat");
        $(this).addClass("active-chat");
        restaurantName = $(this).children(".chat-person").text();
        var messagesOfThisUser = messages[restaurantName];
        var messagesLength = Object.keys(messagesOfThisUser).length;
        for (i = 0; i < messagesLength ; i++){
            messageDate = Object.keys(messagesOfThisUser)[i];
            $(".messages-box").append("<div class = 'messages-date'>" + messageDate + "</div>");
            for (j = 0; j < messagesOfThisUser[messageDate].length; j++){
                theMessage = messagesOfThisUser[messageDate][j]
                sendByUser = theMessage.sendByUser;
                restaurantId = theMessage.restaurantId;
                if (sendByUser == "True"){
                    $(".messages-box").append("<div class = 'message-sent'><div class = 'message-text'>" +
                    theMessage.messageText + "</div>" + "<div class = 'message-time'>" + 
                    theMessage.timestamp + "</div></div>")  
                }
                else{
                    $(".messages-box").append("<div class = 'message-recv'><div class = 'message-text'>" +
                    theMessage.messageText + "</div>" + "<div class = 'message-time'>" + 
                    theMessage.timestamp + "</div></div>")  
                }
                
            }
        }
    })
    $("#send-button").click(function() {
        var text = $("#text-box").val()
        if (text == "" || text == " "){
            return false;
        }
        var url = "/messages/1"; // the script where you handle the form input.
        var dataParams = $("#send-message-form").serializeArray();
        dataParams.push({"name":"restaurantName", "value":restaurantName}
        , {"name":"restaurantId", "value":restaurantId});
        console.log(dataParams)
        $.ajax({
               type: "POST",
               url: url,
               data: dataParams, // serializes the form's elements.
               success: function(data)
               {
                $(".messages-box").append("<div class = 'message-sent'><div class = 'message-text'>" +
                $("#text-box").val() + "</div>" + "<div class = 'message-time'>" + 
                "Now" + "</div></div>")
                $("#text-box").val("");
            }
             });
    
        return false; // avoid to execute the actual submit of the form.
    });
})
