from django.conf import settings


def use_s3(context):
    # add flag to check on template if we should upload to s3
    # on local host
    return {'USE_S3': settings.USE_S3}
