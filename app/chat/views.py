from django.db.models import Q
from django.shortcuts import render

from .forms import ChatForm
from .models import Chat


# Create your views here.

def chat(request):
    form = ChatForm()

    current_user_id = request.user.id
    messages = Chat.objects.filter(Q(sender_id=1, user_id=2) | Q(sender_id=2, user_id=1))
    if request.method == 'POST':
        form = ChatForm(request.POST)
    if form.is_valid():
        form_parsed = form.save(commit=False)
        form_parsed.sender_id = current_user_id
        form_parsed.sender_current_message = request.user
        # TODO: Penser à ajouter le destinataire
        form_parsed.user_id = 1
        form_parsed.save()
    return render(request, "chat/index.html", context={'form': form, 'messages': messages, 'user': request.user})
