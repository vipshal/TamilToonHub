from django import forms
from .models import Video

class Task(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title','description','movie','poster','image',]