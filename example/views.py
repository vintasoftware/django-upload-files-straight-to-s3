# coding: utf-8

from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse_lazy

from example.models import Document
from example.forms import DocumentForm


class DocumentUpload(generic.FormView):
    template_name = 'example/upload_document.html'
    form_class = DocumentForm
    success_url = reverse_lazy('example:document-upload')

    def form_valid(self, form):
        form.save()
        return super(DocumentUpload, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(DocumentUpload, self).get_context_data(*args, **kwargs)
        context['documents'] = Document.objects.all()
        return context
