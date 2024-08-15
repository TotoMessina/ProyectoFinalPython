from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm

@login_required
def message_list(request):
    messages = Message.objects.all()
    return render(request, 'messages/message_list.html', {'messages': messages})

@login_required
def message_detail(request, pk):
    message = Message.objects.get(pk=pk)
    return render(request, 'messages/message_detail.html', {'message': message})

@login_required
def create_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message_list')
    else:
        form = MessageForm()
    return render(request, 'messages/message_form.html', {'form': form})

@login_required
def update_message(request, pk):
    message = Message.objects.get(pk=pk)
    if request.method == 'POST':
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect('message_detail', pk=pk)
    else:
        form = MessageForm(instance=message)
    return render(request, 'messages/message_form.html', {'form': form})

@login_required
def delete_message(request, pk):
    message = Message.objects.get(pk=pk)
    if request.method == 'POST':
        message.delete()
        return redirect('message_list')
    return render(request, 'messages/message_confirm_delete.html', {'message': message})
