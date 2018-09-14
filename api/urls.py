''' urls.py
'''

from django.urls import include
from django.urls import re_path
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

urlpatterns = [
    re_path(r'^$',
            TemplateView.as_view(template_name='index.html'),
            name='index'),
    re_path(r'^robots.txt$',
            TemplateView.as_view(template_name="robots.txt",
                                 content_type="text/plain"),
            name="robots_file"),
    re_path(r'^admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
