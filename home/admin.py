from django.contrib import admin
from .models import LeaveMessage
from django.forms import TextInput, ModelForm, Form
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from phonenumber_field.formfields import SplitPhoneNumberField


# Register your models here.
class LeaveMessageForm(ModelForm):
    class Meta:
        widgets = {
            'phone': PhoneNumberPrefixWidget(widgets=[TextInput(), TextInput()]),
        }


class PhoneForm(Form):
    number = SplitPhoneNumberField()


@admin.register(LeaveMessage)
class LeaveMessageAdmin(admin.ModelAdmin):
    pass
