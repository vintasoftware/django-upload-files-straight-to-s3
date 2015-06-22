from django.conf import settings


def debug(context):
    # allow to check DEBUG flag from a template
    return {'DEBUG': settings.DEBUG}
