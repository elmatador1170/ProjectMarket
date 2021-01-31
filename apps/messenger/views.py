from django.shortcuts import render, reverse
from .forms import Messaging, ChatMessage
from .models import Message, Conversation, Participator
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect


# Create your views here.
def send_message(request):
    """Versenden einer Nachricht."""
    if request.method != 'POST':
        form = Messaging()
    else:
        form = Messaging(data=request.POST)

        recipient_user = list(get_user_model().objects.filter(username=request.POST['recipient']))[0]
        as_sender = list(Message.objects.filter(sender=request.user, recipient=request.POST['recipient']))
        as_recipient = list(Message.objects.filter(sender=recipient_user.id, recipient=request.user))
        conversations = as_sender + as_recipient

        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.sender = request.user

            # Wenn eine Konversation zwischen den beiden Parteien vorhanden ist, dann wird die Nachricht an die
            # Konversation angeknüpft, ansonsten wird eine neue Konversation erschaffen und die Nachricht dann dort
            # angehängt.
            if bool(conversations):
                new_message.parent = conversations[0].parent
            else:
                new_conversation = create_conversation(request, recipient_user)
                new_message.parent = new_conversation

            new_message.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {
        'form': form
    }
    return render(request, 'messenger/send_message.html', context)


def create_conversation(request, recipient):
    """Neue Konversation wird erstellt und Teilnehmer werden hinzugefügt."""
    new_conversation = Conversation()
    new_conversation.save()

    participator1 = Participator(username=request.user.username)
    participator1.save()
    participator1.conversations.add(new_conversation)

    participator2 = Participator(username=recipient.username)
    participator2.save()
    participator2.conversations.add(new_conversation)

    return new_conversation


def show_conversations(request):
    """Alle Konversationen, die der Benutzer geführt hat."""
    information = []

    all_user_conversations = Conversation.objects.filter(participator__username=request.user.username)

    for conversation in all_user_conversations:
        if bool(conversation):
            counterpart = ""
            for participator in list(conversation.participator_set.all()):
                print(participator.username)
                if participator.username != request.user.username:
                    counterpart = participator.username
            all_messages = conversation.message_set.all()
            last_message = all_messages[len(all_messages)-1]

            data = {
                'conversation_id': conversation.id,
                'counterpart': counterpart,
                'last_message': last_message,
                'date_sent': last_message.date_sent,
            }
            information.append(data)

    context = {
        'information': information
    }
    return render(request, 'messenger/conversations.html', context)


def show_conversation(request, conversation_id):
    conversation = Conversation.objects.filter(pk=conversation_id)[0]
    messages = list(conversation.message_set.all().order_by('date_sent'))
    participants = list(conversation.participator_set.all())
    counterpart = ""
    for participator in list(conversation.participator_set.all()):
        if participator.username != request.user.username:
            counterpart = participator.username

    context = {
        'conversation': conversation,
        'messages': messages,
        'counterpart': counterpart,
        'form': send_message_chat(request, conversation_id, counterpart)
    }
    return render(request, 'messenger/conversation.html', context)


def send_message_chat(request, conversation_id, recipient):
    conversation = Conversation.objects.get(pk=conversation_id)

    """Eine Nachricht im Chat versenden."""
    if request.method != 'POST':
        form = ChatMessage()
    else:
        form = ChatMessage(data=request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.sender = request.user
            new_message.recipient = recipient
            new_message.parent = conversation
            new_message.save()

    return form
