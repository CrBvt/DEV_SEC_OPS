from django.urls.conf import re_path

from django.urls import path
from .views import DocsRootView, serve_docs, DOCS_DIRHTML

urlpatterns = [
    # path('docs/', DocsRootView.as_view(permanent=True), name='doc_index')
]

if not DOCS_DIRHTML:
    urlpatterns += [
        re_path(r'^$', DocsRootView.as_view(permanent=True), name='docs.index'),
    ]

urlpatterns += [
    re_path(r"^(?P<path>.*)$", serve_docs, name="docs.files"),
]