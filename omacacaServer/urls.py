"""omacacaServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from ltbm import views

# drf_yasg 从这里开始
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Omacaca Server API",
        default_version='v1.0',
        description="Omacaca Server 接口文档",
        # terms_of_service="https://www.omacaca.com",
        contact=openapi.Contact(email="296554555@qq.com"),
        license=openapi.License(name="GPL", url="https://www.gnu.org/licenses/"),
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,),  # 权限类
)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('ltbm/', include('ltbm.urls')),
]
