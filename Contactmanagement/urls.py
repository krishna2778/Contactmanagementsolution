from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Contactmanagement.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$','contactapp.views.home'),
    url(r'^contact/$','contactapp.views.contactpage'),
    url(r'^add_contact/$','contactapp.views.addcontact'),
    url(r'^display_contact/$','contactapp.views.displaycontact'),
    url(r'^display_contact/(\w)$','contactapp.views.displaycontact_alphabet'),
)
