from django.forms import ModelForm
from django import forms
# from django.contrib.auth.models import User
from .models import User

privacy = (
        ("True", "Public"),
        ("False" , "Private")
    )

class form_for_thoughts(forms.Form):
    user = forms.CharField(required=True)
    name  = forms.CharField(label= "Name  of your tweet", required=True,max_length=50)
    content = forms.CharField(required=True, label= "Content")
    file = forms.FileField()
    is_public = forms.ChoiceField(choices = privacy )
   

class CommentForm(forms.Form):
    text = forms.CharField(label="Your Comment..", required=True, widget=forms.Textarea())

class SharePostForm(forms.Form):
    shared_with = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple,required=False)
