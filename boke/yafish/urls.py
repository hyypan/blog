from django.conf.urls import url
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from yafish.api.articles_api import ArticleViewSet
from boke import settings
router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
urlpatterns = [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+router.urls


print('urlpatterns', urlpatterns)
