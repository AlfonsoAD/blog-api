from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsAdminOrReadOnly


class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    # queryset = Category.objects.all()
    # filtro para solo los activos/published
    queryset = Category.objects.filter(published=True)
    lookup_field = 'slug'
    # filtrar por titulo
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
