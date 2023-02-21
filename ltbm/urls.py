from django.urls import path, re_path
from . import views
from rest_framework import routers

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

urlpatterns = [
    path('degtable', views.DegTableView.as_view()),
    path('gpftable', views.DegEnrichView.as_view()),
    path('gseatable', views.GseaEnrichView.as_view()),
    path('deghtmtable', views.DegHtmView.as_view()),
    path('degstktable', views.DegStkView.as_view()),
    path('metainfo', views.MetaTableView.as_view()),
    path('metaumap', views.UmapTableView.as_view()),
    path('vpatable', views.VpaTableView.as_view()),
    path('geneexp', views.GeneVstExpTableView.as_view()),
    path('geneexpgroupby', views.GeneVstExpGroupByView.as_view()),
    path('tsares', views.TsaResView.as_view()),
    path('wgcnamttable', views.WgcnaMtTableView.as_view()),
    path('wgcnares', views.WgcnaResView.as_view()),

]

router = routers.DefaultRouter()
router.register('test', views.BookView)
# path('degtable', views.DegTableView, name="product-list")
urlpatterns += router.urls
# 分页
# router.register(r'^degtable', views.DegTableView({'get': 'get_all'}))
