from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from yolov5 import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

#routers
router = DefaultRouter()
router.register(r'upload',views.ImagetoNumberviewset)

# from rest_framework.schemas import get_schema_view #schima va dokumentla
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


#dokumitatsiya
schema_view = get_schema_view(
    openapi.Info(
        title='Number API',
        description="Number API",
        default_version='v1',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email="xackercoder@gmail.com"),
        license=openapi.License(name='API lisensiyasi')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
    
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # redoc
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)