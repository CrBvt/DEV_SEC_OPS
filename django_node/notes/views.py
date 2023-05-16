from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView

# Create your views here.

from .models import Notes

class NotesListView(ListView):
    model = Notes
    context_object_name = 'note_list'
    template_name = 'notes/template/note_list.html'

# def list(request):
#     note_list = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'note_list': note_list})

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/template/note_details.html'

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist")
#
#     return render(request, 'notes/note_details.html', {'note': note})