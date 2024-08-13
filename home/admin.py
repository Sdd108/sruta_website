from django.contrib import admin
from .models import LeaveMessage
from django.forms import TextInput, ModelForm
from phonenumber_field.widgets import PhoneNumberPrefixWidget


# Register your models here.
class LeaveMessageForm(ModelForm):
    class Meta:
        widgets = {
            'phone': PhoneNumberPrefixWidget(widgets=[TextInput(), TextInput()]),
        }


@admin.register(LeaveMessage)
class LeaveMessageAdmin(admin.ModelAdmin):
    pass
