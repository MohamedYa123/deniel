from django.urls import path,include
from .views import *
from django.conf.urls.static import static
urlpatterns=[

    path('',homepage,name="home"),

]+ static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)