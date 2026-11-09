from django.contrib import admin
from django.urls import include, path
# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView  # API

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # API
    # path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # API
    path('', include('main.urls')),
]
