from ltbm.serializers import degser
from ltbm.models import DegTable
# 和 终极封装 ViewModelSet
from rest_framework.viewsets import ModelViewSet


class DegTableView(ModelViewSet):
    queryset = DegTable.objects.all()
    serializer_class = degser.DegTableSerializers

# 但是封装的越多，导致代码的灵活性越低，在需要的时候需要基于基类自行修改而不是使用最后的封装
