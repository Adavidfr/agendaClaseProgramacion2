from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Contacto

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserCreationForm
        fields = ['username', 'email', 'password1', 'password2']
        
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'telefono', 'email']