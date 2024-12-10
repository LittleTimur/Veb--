from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from our_models.models import Message, Profile
from our_models.views import Get_Profile_by_user
from chat.forms import MessageForm
from django.http import HttpResponseRedirect

@login_required
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    context = {'messageRequests': messageRequests, 'unreadCount': unreadCount}
    return render(request, 'inbox.html', context)


@login_required
def viewMessage(request, pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()
    context = {'message': message}
    return render(request, 'message.html', context)


@login_required
def createMessage(request, user_id):
    recipient = Get_Profile_by_user(user_id=user_id)
    form = MessageForm()

    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.surname = sender.surname
            message.save()

            messages.success(request, 'Your message was successfully sent!')
            return HttpResponseRedirect("/SRAST")

    context = {'recipient': recipient, 'form': form}
    return render(request, 'message_form.html', context)    
