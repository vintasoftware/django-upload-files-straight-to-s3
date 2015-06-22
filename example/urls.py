# coding: utf-8

from django.conf.urls import patterns, include, url

from example.endpoints import S3AuthAPIView
from example.views import DocumentUpload


urlpatterns = patterns('',
    url(r'^documents/s3auth/$', S3AuthAPIView.as_view(),
        name='s3-sign'),
    url(r'^documents/upload/$', DocumentUpload.as_view(),
        name='document-upload'),
)
