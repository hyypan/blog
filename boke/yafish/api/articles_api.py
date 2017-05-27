from rest_framework import serializers, viewsets, permissions
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response

from yafish import models as m


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Article
        fields = ('id', 'created', 'modified', 'title', 'second_title', 'author', 'icon', 'content', 'read_times',
                  'good_click', 'plate')


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = m.Article.objects.all()
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    permission_classes = ()

    @list_route(methods=['get'])
    def get_articles_by_page(self, request):
        """根据页数和标签获取文章"""

        page = request.query_params.get('page')
        plate = request.query_params.get('plate')
        return Response(page)
