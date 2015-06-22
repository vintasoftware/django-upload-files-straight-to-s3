# coding: utf-8

from django import forms
from django.forms import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from example.models import Document


class DocumentForm(forms.ModelForm):
    file_name = forms.CharField(widget=forms.HiddenInput, required=False)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 's3upload-form'
        self.helper.add_input(Submit('submit', 'Submit'))
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['doc_file'].required = False

    def clean(self):
        file_name = self.cleaned_data.get('file_name')
        doc_file = self.cleaned_data.get('doc_file')
        if not doc_file and not file_name:
            self.add_error(
                'doc_file',
                ValidationError(self.fields['doc_file']
                                .error_messages['required'], code='required'))
        elif not doc_file and file_name:
            self.cleaned_data['doc_file'] = file_name
        return super(DocumentForm, self).clean()

    class Meta:
        model = Document
        fields = ('id', 'name', 'doc_file', 'file_name')
