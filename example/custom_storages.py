# coding: utf-8

from storages.backends.s3boto import S3BotoStorage


class StaticCachedS3BotoStorage(S3BotoStorage):

    def __init__(self, *args, **kwargs):
        kwargs['location'] = 'static'
        kwargs['querystring_auth'] = False

        super(StaticCachedS3BotoStorage, self).__init__(*args, **kwargs)


class MediaS3BotoStorage(S3BotoStorage):

    def __init__(self, *args, **kwargs):
        kwargs['location'] = 'media'
        kwargs['querystring_auth'] = True
        kwargs['acl'] = 'private'

        super(MediaS3BotoStorage, self).__init__(*args, **kwargs)
