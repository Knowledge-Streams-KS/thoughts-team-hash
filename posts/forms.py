from django.forms import ModelForm
from django import forms

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
   
