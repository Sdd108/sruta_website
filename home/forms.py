from django import forms
from .models import LeaveMessage


class LeaveMessageForm(forms.ModelForm):
    class Meta:
        model = LeaveMessage
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter your name...'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'name@example.com'}
            ),
            'phone': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '+86 186 8888 6666'}
            ),
            'message': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Enter your message here...', 'style': 'height: 10rem'}
            ),
        }
