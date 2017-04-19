from __future__ import unicode_literals
from model_utils import models as util_models
from django.db import models

# Create your models here.


class ArticleType(util_models.TimeStampedModel):
    name = models.CharField(verbose_name='文章类型', max_length=100, help_text='具体分类')


class Article(util_models.TimeStampedModel):
    title = models.CharField(verbose_name='文章标题', max_length=200, help_text='字数不超过200字')
    second_title = models.CharField(verbose_name='文章副标题', max_length=200, help_text='字数200字以下')
    author = models.CharField(verbose_name='作者', max_length=50, help_text='中英文都可以')
    artice_type = models.ForeignKey(ArticleType, verbose_name='文章类型')
    icon = models.ImageField(verbose_name='文章相关图片')
    content = models.TextField(verbose_name='文章内容')
