from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from musicstore import views
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^accounts/register/$','musicstore.views.register_user'),
    url(r'^accounts/register_success/$','musicstore.views.register_success'),
    url(r'^accounts/invalid/$','musicstore.views.invalid_login'),
    url(r'^accounts/loggedin/$','musicstore.views.loggedin'),
    url(r'^accounts/logout/$','musicstore.views.logout'),
    url(r'^accounts/auth/$','musicstore.views.auth_view'),
    url(r'^accounts/login/$','musicstore.views.login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^trending/(?P<value>\w+)','musicstore.views.TrendingCatagory'),
    url(r'^trending/$','musicstore.views.Trending'),
    url(r'^addtoplaylist/$',views.ADDtoPlaylist,name="Shalok testing server"),
    url(r'^$',views.MAIN,name="Shalok testing server"),
    url(r'^album/(?P<album>\d+)/(?P<value>\d+)$',views.filterAlbum,name="Shalok testing server"),
    url(r'^song/(?P<song>\d+)/$',views.filterSong,name="Shalok testing server"),
    #url(r'^<value>',views.ALBUM,name="album"),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
