from ltbm.serializers import degser
from ltbm.models import DegTable
from ltbm.filter import DegTableFilter
# 和 终极封装 ViewModelSet
from rest_framework.viewsets import ModelViewSet


class DegTableView(ModelViewSet):
    queryset = DegTable.objects.all()
    serializer_class = degser.DegTableSerializers
    filter_class = DegTableFilter  # 过滤类

# 但是封装的越多，导致代码的灵活性越低，在需要的时候需要基于基类自行修改而不是使用最后的封装


# 模块导入
# from rest_framework.pagination import PageNumberPagination,CursorPagination,LimitOffsetPagination

# PageNumberPagination  常规分页
# LimitOffsetPagination  偏移分页
# CursorPagination  游标分页

# class Book(ViewSetMixin, APIView):
#     def get_all(self, request):
#         response = {'status': 100, 'msg': '查询成功'}
#         book_list = models.Book.objects.all()
#         # 实例化产生一个分页对象
#         # 不继承来修改对象的值
#         page=PageNumberPagination()
#         page.page_size=2   # 每页显示的个数
#         page.page_query_param='pag'    # 路由中？后面的key，指定页码
#         page.page_size_query_param = 'size'   # 指定当前页显示多少条
#         page.max_page_size = 5  # 每页最多显示多少条
#         # 第一个参数:要分页的数据,第二个参数request对象,第三个参数,当前视图对象
#         page_list = page.paginate_queryset(book_list, request, self)
#         # 再序列化的时候,用分页之后的数据
#         ser = mySer.BookSerializer(instance=page_list, many=True)
#         # 会带着链接,和总共的条数(不建议用,会把总数据条数返回)
#         # return page.get_paginated_response(ser.data)
#         return Response(ser.data)
