from django.conf.urls import url
from django.conf.urls.static import static

from boke import settings

urlpatterns = [

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

print('urlpatterns', urlpatterns)
