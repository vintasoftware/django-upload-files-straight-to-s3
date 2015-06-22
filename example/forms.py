# coding: utf-8

from django import forms
from django.forms import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from example.models import Document


class DocumentForm(forms.ModelForm):
    # since we are not going to send the file via POST we need a field to save
    # the already uploaded path of the uploaded file.
    file_name = forms.CharField(required=False)

    class Meta:
        model = Document
        fields = ('id', 'name', 'doc_file', 'file_name')

    def __init__(self, *args, **kwargs):
        # crispy forms
        self.helper = FormHelper()
        self.helper.form_class = 's3upload-form'
        self.helper.add_input(Submit('submit', 'Submit'))
        super(DocumentForm, self).__init__(*args, **kwargs)
        # doc_file is not required if file_name is set
        self.fields['doc_file'].required = False
        self.fields['file_name'].widget.attrs['readonly'] = True

    def clean(self):
        file_name = self.cleaned_data.get('file_name')
        doc_file = self.cleaned_data.get('doc_file')
        # if doc_file and file_name is not set we are missing the file
        if not doc_file and not file_name:
            self.add_error(
                'doc_file',
                ValidationError(self.fields['doc_file']
                                .error_messages['required'], code='required'))
        # if file_name is set with the path of the file it was uploaded by
        # the frontend
        elif not doc_file and file_name:
            self.cleaned_data['doc_file'] = file_name
        return super(DocumentForm, self).clean()
