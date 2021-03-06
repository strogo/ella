from django.conf import settings
from django.contrib.sites.models import Site
from django.template.defaultfilters import slugify
from ella.core.middleware import ECACHE_INFO


MEDIA_URL = getattr(settings, 'MEDIA_URL', '')
VERSION = getattr(settings, 'VERSION', 1)
SERVER_INFO = getattr(settings, 'SERVER_INFO', {})

current_site = Site.objects.get_current()
current_site_name = slugify(current_site.name)


def url_info(request):
    """
    Make MEDIA_URL and current HttpRequest object
    available in template code.
    """

    return {
        'MEDIA_URL' : MEDIA_URL,
        'VERSION' : VERSION,
        'SERVER_INFO' : SERVER_INFO,
        'SITE_NAME' : current_site_name,
        'CURRENT_SITE': current_site,
    }

def cache(request):

    if not hasattr(request, '_cache_middleware_key'):
        return {}

    return {
        ECACHE_INFO: getattr(request, '_cache_middleware_key'),
    }
