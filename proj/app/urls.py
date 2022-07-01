from django.urls import path,include
from .views import *
from django.conf.urls.static import static
urlpatterns=[
    path('Login/',Login,name="login"),
    path('Logout/',Logout,name="logout"),
    path('',homepage,name="home"),
    path('<int:l>',homepage2,name="home"),
    path('create/',createapharmacy,name="create"),
    path('pharmacy/<int:id>/',pharmacyshow,name='pharmacy'),
    path('pharmacy/edit/<int:id>/',editapharmacy,name='editapharmacy'),
    path('pharmacy/uploadimage/<int:id>/',uploadapharmacy,name='uploadapharmacy'),
    path('register/',register,name="register"),
    path('requestwork/<int:phid>/',requestwork,name="requestwork"),
    path('request/<int:id>/',requestview,name="requestview"),
    path('viewrequests/<str:tr>',viewrequests,name="viewrequests"),
    path('refuserequest/<int:rid>',refuserequest,name="refuserequest"),
    path('acceptrequest/<int:rid>',acceptrequest,name="acceptrequest"),
    path('profile/edit',editprofile,name="editprofile"),
    path('profile/uploadImage',uploadprofile,name="uploadprofile"),
    path('profile/<int:id>',profile,name="profile"),
]+ static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)