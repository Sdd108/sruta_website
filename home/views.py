from django.shortcuts import render, redirect
from .forms import LeaveMessageForm
from django.views.generic import FormView


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # 取第一个IP地址
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def leave_message_view(request):
    success_message = None
    if request.method == 'POST':
        form = LeaveMessageForm(request.POST)
        if form.is_valid():
            client_ip = get_client_ip(request)
            # 不直接使用 form.save()，而是创建一个模型实例，手动设置 ip_address
            leave_message = form.save(commit=False)
            leave_message.client_ip = client_ip  # 保存客户端 IP
            leave_message.save()
            success_message = "Message submitted successfully"
            form = LeaveMessageForm()  # 重置表单，方便用户提交另一个留言
    else:
        form = LeaveMessageForm()

    return render(request, 'index.html', {'form': form, 'success_message': success_message})
