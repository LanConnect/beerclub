from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'beerclub.beer.views.home', name='home'),
    url(r'^beer/$', 'beerclub.beer.views.home', name='home'),
    url(r'^beer/user/$', 'beerclub.beer.views.user', name='user'),
	url(r'^beer/drink/$', 'beerclub.beer.views.drink', name='drink'),
	#url(r'^beer/drink/(?<user_barcode>[0-9A-Z]+)/$', 'beerclub.beer.views.drink', name='drink'),
	# url(r'^beerclub/', include('beerclub.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
