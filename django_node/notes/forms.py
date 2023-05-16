from django import forms
from django.core.exceptions import ValidationError

from .models import Notes


class NotesForm(forms.ModelForm):

    class Meta:
        model = Notes
        fields = {'title', 'text'}

    def clean_title(self):

        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError("Type Django in title please")
        return title

