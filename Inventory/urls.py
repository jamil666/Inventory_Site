from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from Inventory import views

urlpatterns = [

        url(r'^$', views.main, name='Main'),
        url(r'^addnew$', views.AddNew, name='AddNew'),
        url(r'^edit', views.Edit, name='Edit'),
        url(r'^delete$', views.Delete, name="Delete")

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
