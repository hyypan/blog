"""boke URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import coreapi
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import renderers, schemas, response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.documentation import include_docs_urls, get_schemajs_view, get_docs_view
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework_swagger.views import get_swagger_view

import yafish.urls
from boke import settings

# generator = SchemaGenerator(title='Stock Prices API')
# @api_view()
# @renderer_classes([renderers.CoreJSONRenderer])
# def schema_view(request):
#     generator = schemas.SchemaGenerator(title='Bookings API')
#     return Response(generator.get_schema())
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
schema_view = get_swagger_view(title='yafish')
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^yafish/', include('yafish.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^swagger/', schema_view),
    url(r'^docs/', include_docs_urls(title='blog', description='yafish')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.BASE_URL, document_root=settings.MEDIA_ROOT)
