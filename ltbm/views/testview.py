from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ltbm.serializers import BookSerializers
from ltbm.models import Book

# 最基础的APIView 重写了request 和 response 的相关逻辑
# class BookView(APIView):
#
#     def get(self, request):
#         # 获取所有的书籍
#         book_list = Book.objects.all()
#         # 构建序列化器对象:
#         serializer = BookSerializers(book_list, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         # 获取请求数据
#         # print("data", request.data)
#         # 构建序列化器对象
#         serializer = BookSerializers(data=request.data)
#         # 校验数据
#         if serializer.is_valid():  # 返回一个布尔值，所有字段皆通过才返回True，遍历成功值在validated_data中，错误键与原因在errors中
#             # 数据校验通将数据插入到数据库中
#             # new_book = Book.objects.create(**serializer.validated_data)
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             # 校验失败
#             return Response(serializer.errors)
#
#
# class BookDetailView(APIView):
#     def get(self, request, id):
#         book = Book.objects.get(pk=id)
#         serializer = BookSerializers(instance=book, many=False)
#
#         return Response(serializer.data)
#
#     def put(self, request, id):
#         # 获取提交的更新数据
#         # print( "data: ", request.data)
#         update_book = Book.objects.get(pk=id)  # 构建序列化器对象
#         serializer = BookSerializers(instance=update_book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)  # 针对serializer.instance序列化
#         else:
#             return Response(serializer.errors)
#
#     def delete(self, request, id):
#         Book.objects.get(pk=id).delete()
#         return Response()

# 使用 GenericAPIView 封装了每次要传入的模型类和序列化器
# from rest_framework.generics import GenericAPIView
#
#
# class BookView(GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
#
#     def get(self, request):
#         # 构建序列化器对象:
#         serializer = self.get_serializer(instance=self.get_queryset(), many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         # 构建序列化器对象
#         serializer = self.get_serializer(data=request.data)
#         # 校验数据
#         if serializer.is_valid():  # 返回一个布尔值，所有字段皆通过才返回True，遍历成功值在validated_data中，错误键与原因在errors中
#             # 数据校验通将数据插入到数据库中
#             # new_book = Book.objects.create(**serializer.validated_data)
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             # 校验失败
#             return Response(serializer.errors)
#
#
# class BookDetailView(GenericAPIView):
#     def get(self, request, pk):
#         serializer = self.get_serializer(instance=self.get_object(), many=False)
#
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         serializer = self.get_serializer(instance=self.get_object(), data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)  # 针对serializer.instance序列化
#         else:
#             return Response(serializer.errors)
#
#     def delete(self, request, pk):
#         self.get_object().delete()
#         return Response()


# Mixin类 封装增删改查查的逻辑

# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
#     DestroyModelMixin
#
#
# class BookView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#
# class BookDetailView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers

#     def get(self, request, pk):
#         return self.retrieve(request, pk)
#
#     def put(self, request, pk):
#         return self.update(request, pk)
#
#     def delete(self, request, pk):
#         return self.destroy(request, pk)

# Mixin在进行小的封装
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
#
#
# class BookView(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
#
#
# class BookDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers

# ViewSet: ViewSetMixin使得view中的5种方法可以写到一个类里面，自定义url中的参数，使得对应的method分发到自定义的方法中
# 但是默认的ViewSet封装的是APIView，需要自己写5种方法，因此再封装GenericAPIView
# from rest_framework.viewsets import ViewSet, GenericViewSet
# from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
#     DestroyModelMixin
#
#
# class BookView(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,
#                DestroyModelMixin):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers

# 和 终极封装 ViewModelSet
from rest_framework.viewsets import ModelViewSet


class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

# 但是封装的越多，导致代码的灵活性越低，在需要的时候需要基于基类自行修改而不是使用最后的封装
