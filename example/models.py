from django.db import models

import uuid


def document_upload_path(instance, filename):
    return 'documents/{}/{}'.format(uuid.uuid4(),
                                    filename)


# Create your models here.
class Document(models.Model):
    name = models.CharField(max_length=100)
    doc_file = models.FileField(upload_to=document_upload_path)
