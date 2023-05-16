from django.shortcuts import render
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notes
from .forms import NotesForm

class NotesDeleteView(DeleteView):
    model = Notes
    context_object_name = "note"
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

class NotesUpdateView(UpdateView):
    model = Notes
    context_object_name = "note"
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = Notes
    context_object_name = "note"
    success_url = '/smart/notes'
    form_class = NotesForm

    def form_valid(self, form):

        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'note_list'
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()

    # template_name = 'notes/templates/note_list.html'

# def list(request):
#     note_list = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'note_list': note_list})


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    # template_name = 'notes/templates/note_detail.html'

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist")
#
#     return render(request, 'notes/note_details.html', {'note': note})