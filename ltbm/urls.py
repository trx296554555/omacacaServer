from django.urls import path, re_path
from . import views
from rest_framework import routers

urlpatterns = []
# APIView 无名分组传参 按顺序来
# urlpatterns = [
#     path('test', views.BookView.as_view()),
#     re_path(r'test/(\d+)', views.BookDetailView.as_view())
# ]

# GenericAPIView 有名分组传参
# urlpatterns = [
#     path('test', views.BookView.as_view()),
#     re_path(r'test/(?P<pk>\d+)', views.BookDetailView.as_view())
# ]


# ViewSet  ViewSetMixin 重写了as_view 使得可以传参，使得在请求时，对应的method替换为自定义的方法
# urlpatterns = [
#     path('test', views.BookView.as_view({"get": "list", "post": "create"})),
#     re_path(r'test/(?P<pk>\d+)',
#             views.BookView.as_view({"get": "retrieve", "put": "update", "delete": "destory"}))
# ]

router = routers.DefaultRouter()
router.register('test', views.BookView)

urlpatterns += router.urls
