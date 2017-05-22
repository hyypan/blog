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

    @list_route(methods=['post'])
    def bbb(self, request):
        """
        This text is the description for this API.
        ---
        parameters:
        - name: icon
          description: Foobar long description goes here
          required: true
          type: string
          paramType: form
        - name: other_foo
          paramType: query
        - name: other_bar
          paramType: query
        - name: avatar
          type: file
        """
        return Response({'aaaa'})

    @list_route(methods=['post'])
    def aaa(self, request):
        """
        
        """
        pass