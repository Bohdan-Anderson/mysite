from django.conf.urls.defaults import *
from mysite.views import hello, current_datetime, hours_ahead, site_directories, images, display_meta,makeSvg
from django.contrib import admin
from walk import views
admin.autodiscover()

urlpatterns = patterns('',
    ('^hello/$', hello),
	('^time/$', current_datetime),
	(r'^time/plus/(\d{1,2})/$', hours_ahead),
	(r'^directories/$', site_directories),
	(r'^image/(\w+/)$', images),
	(r'^admin/', include(admin.site.urls)),
	(r'^meta/$',display_meta), 
	(r'^search-form/$', views.search),
	(r'^search/$', views.search),
	(r'^make-SVG/$', makeSvg),
)
