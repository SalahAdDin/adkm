import os

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from django.views.generic.base import RedirectView

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailsearch import urls as wagtailsearch_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls

from wagtail.wagtailimages import urls as wagtailimages_urls
from wagtail.wagtailembeds import urls as wagtailembeds_urls
from wagtail.wagtailsnippets import urls as wagtailsnippets_urls
from wagtail.wagtailredirects import urls as wagtailredirects_urls
from wagtail.contrib.wagtailsitemaps.views import sitemap

urlpatterns = patterns('',
    url(r'^django-admin/', include(admin.site.urls)),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^search/', include(wagtailsearch_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    
    url(r'^embeds/', include(wagtailembeds_urls)),
    url(r'^images/', include(wagtailimages_urls)),
    url(r'^redirects/', include(wagtailredirects_urls)),    
    url(r'^snippets/', include(wagtailsnippets_urls)),
    url('^sitemap\.xml$', sitemap),
    #url(r'^users/', include(wagtailusers_urls)),
    
    url(r'', include(wagtail_urls)),
)


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
    #urlpatterns += patterns('',
    #    (r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'myapp/images/favicon.ico'))
    #)
