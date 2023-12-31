import re
from django.urls import  re_path
from urllib.parse import urlsplit
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.views.static import serve

def images_server(images_url : str,images_location : str ):
    view = serve 
    if not images_url:
        raise ImproperlyConfigured("Настройки image_server неверны")
    elif urlsplit(images_url).netloc:
        return []
    return [
        re_path(
            r"^%s(?P<path>.*)$" % re.escape(images_url.lstrip("/")), view, kwargs={
                "document_root" : images_location
            }
        ),
]