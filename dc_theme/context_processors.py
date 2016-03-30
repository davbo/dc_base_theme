from django.conf import settings


def dc_theme_context(request):
    return {
        'site_title': getattr(settings, 'SITE_TITLE', 'Democracy Club')
    }
