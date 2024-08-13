from django.shortcuts import render, redirect
from .forms import LeaveMessageForm
from django.views.generic import FormView


def leave_message_view(request):
    success_message = None
    if request.method == 'POST':
        form = LeaveMessageForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Message submitted successfully"
            form = LeaveMessageForm()  # 重置表单，方便用户提交另一个留言
    else:
        form = LeaveMessageForm()

    return render(request, 'index.html', {'form': form, 'success_message': success_message})
