from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from Inventory import views
from django.contrib.auth import views as auth_views


urlpatterns = [

        url(r'^$', views.Login, name='login'),
        url(r'^addnew$', views.AddNew, name='AddNew'),
        url(r'^edit', views.Edit, name='Edit'),
        url(r'^delete$', views.Delete, name="Delete"),
        url(r'^main$', views.main, name="main"),

        url(r'^login/$', views.Login, name='login'),
        url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
