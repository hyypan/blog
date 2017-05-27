from rest_framework import serializers, viewsets
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

    @list_route(methods=['get'])
    def get_articles_by_page(self, request):

        page = request.data.get('page')
        return Response('ok')
