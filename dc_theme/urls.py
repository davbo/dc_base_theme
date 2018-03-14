from django.conf.urls import url

from django.views.generic import TemplateView
from django.views.defaults import page_not_found, server_error


urlpatterns = [
    url(
        r'^$',
        TemplateView.as_view(template_name="html_tester/all_elements.html"),
        name='html_tester'
    ),
    url(r'500.html$', server_error),
    url(r'404.html$', page_not_found, {'exception': "Fake problem"}),
]
