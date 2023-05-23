""" Notes views """

# from django.shortcuts import render
# from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notes
# from django_node.notes.models import Notes
from .forms import NotesForm


class NotesDeleteView(DeleteView):
    """ Notes Delete View """

    model = Notes
    context_object_name = "note"
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'


class NotesUpdateView(LoginRequiredMixin, UpdateView):
    """ Notes Update View """

    model = Notes
    context_object_name = "note"
    success_url = '/smart/notes'
    login_url = "/login"
    form_class = NotesForm


class NotesCreateView(LoginRequiredMixin, CreateView):
    """ Notes Create View """

    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = "/login"
    context_object_name = "note"

    def form_valid(self, form):
        self.object = form.save(commit=False)  # noqa
        self.object.user = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    """ Notes List View """

    model = Notes
    context_object_name = 'note_list'
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()

    # template_name = 'notes/templates/note_list.html'


# def list(request):
#     note_list = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'note_list': note_list})


class NotesDetailView(LoginRequiredMixin, DetailView):
    """ Notes Detail View """

    model = Notes
    context_object_name = 'note'
    login_url = '/login'
    # template_name = 'notes/templates/note_detail.html'

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist")
#
#     return render(request, 'notes/note_details.html', {'note': note})
