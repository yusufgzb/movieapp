from django import forms 
from django.forms import widgets
from .models import Comment

#Filmlere Yorum yapma formu
class ComentForm(forms.ModelForm):
    class Meta:
        #Yıldız için değişkenler
        numbers=(
            ('1','1 Yıldız'),
            ('2','2 Yıldız'),
            ('3','3 Yıldız'),
            ('4','4 Yıldız'),
            ('5','5 Yıldız'),

        )
        # Yorum modelini modele atadık bu şekilde db deki değişkenlere ulaşabiliyoruz
        model = Comment
        #fields = ['full_name','email','text','raing']
        exclude = ['movie',]
        labels = {
            "full_name":"Ad Soyad",
            "email":"Eposta",
            "text":"Yorum",
            "rating":"Puan"
        }
        widgets = {
            "full_name":widgets.TextInput(attrs={"class":"form-control"}),
            "email":widgets.EmailInput(attrs={"class":"form-control"}),
            "text":widgets.Textarea(attrs={"class":"form-control"}),
            "rating":widgets.Select(attrs={"class":"form-control custom-select"},choices=numbers),

        }