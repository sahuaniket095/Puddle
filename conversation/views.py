from django.shortcuts import render,get_object_or_404,redirect
from item.models import Item
from .models import conversation
from .forms import ConversationMessageForm
# Create your views here.

def new_Conversation(request,item_pk):
    item=get_object_or_404(Item,pk=item_pk)
    if item.created_by==request.user:
        return redirect('dashboard:dashboard')
    
    conversations= conversation.objects.filter(item=item).filter(members__in=[request.user.id])
    
    if conversations:
       return redirect('conversation:detail',pk=conversations.first().id)

    if request.method=='POST':
        form=ConversationMessageForm(request.POST)

        if form.is_valid():
            Conversation = conversation.objects.create(item=item)
            Conversation.members.add(request.user)
            Conversation.members.add(item.created_by)
            Conversation.save()

            conversation_message=form.save(commit=False)
            conversation_message.conversation=Conversation
            conversation_message.created_by=request.user
            conversation_message.save()
            return redirect('item:detail',pk=item_pk)
    else:
            form=ConversationMessageForm()

    return render(request,'new.html',{'form':form})    


def inbox(request):
     conversations=conversation.objects.filter(members__in=[request.user.id])
     return render(request,'inbox.html',{'conversations':conversations})


def detail(request,pk):
     conversations=conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
     if request.method=='POST':
          form=ConversationMessageForm(request.POST)

          if form.is_valid():
               conversation_message=form.save(commit=False)
               conversation_message.conversation=conversations
               conversation_message.created_by=request.user
               conversation_message.save()
               conversations.save()
               return redirect('conversation:detail',pk=pk)
     else:    
          form=ConversationMessageForm()

     return render(request,'detail.html',{'conversation':conversations,'form':form})




