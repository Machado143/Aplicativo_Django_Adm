from django.forms import ModelForm, ValidationError
from django.db import models
from django import forms
from Farmacia.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post    
        exclude = ['data_postagem', 'autor', 'aprovado']

    def clean_mensagem(self):
        data = self.cleaned_data["mensagem"]
        if len(data) < 10:
            raise ValidationError("Precisa ter mais de 10 caracteres!")
        
        data = str(data).strip()
        return data