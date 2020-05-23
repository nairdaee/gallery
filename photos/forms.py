from django import forms  #when creating your own model forms
from . import models


class CreatePhoto(forms.ModelForm):
    class Meta: #defines fields to be present and from which model they will be inherited.
        model = models.Photos
        fields = ['title','body','slug','thumb']