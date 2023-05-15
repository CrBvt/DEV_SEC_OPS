from django.shortcuts import render
from django.http import Http404

# Create your views here.

from .models import Notes

def list(request):
    note_list = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'note_list': note_list})

def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")

    return render(request, 'notes/note_details.html', {'note': note})