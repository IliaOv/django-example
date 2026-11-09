from django.urls import path
from . import views
# from django.urls import include  # API
# from rest_framework.routers import DefaultRouter  # API
# router = DefaultRouter()  # API
# router.register('people', views.PersonViewSet, basename='person')  # API

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # path('api/', include(router.urls)),  # API
]
