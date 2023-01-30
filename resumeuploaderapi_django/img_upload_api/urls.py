from django.urls import path,include
# from django.conf import settings
# from django.conf.urls.static import static
from img_upload_api import views

urlpatterns = [
    path('resume/',views.ProfileView.as_view(),name='resume'),
    path('list/',views.ProfileView.as_view(),name='list'),
]