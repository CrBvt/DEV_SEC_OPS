""" Notes forms """

from django import forms
# from django.core.exceptions import ValidationError

from .models import Notes
# from django_node.notes.models import Notes

class NotesForm(forms.ModelForm):

    """ Notes main form """

    class Meta:

        """ ModelForm Meta for NotesForm"""

        model = Notes
        fields = {'title', 'text'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control mb-5'})
        }
        labels = {
            'title': 'Name',
            'text': 'Description'
        }

    # def clean_title(self):
    #
    #     title = self.cleaned_data['title']
    #     if 'Django' not in title:
    #         raise ValidationError("Type Django in title please")
    #     return title
