from __future__ import unicode_literals

from django.core.files.storage import FileSystemStorage
from model_utils import models as util_models
from django.db import models

# Create your models here.


class BannerStorage(FileSystemStorage):
    from boke import settings

    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.BASE_URL, file_permissions_mode=None,
                 directory_permissions_mode=None):
        super(BannerStorage, self).__init__(location=location, base_url=base_url, file_permissions_mode=None,
                                            directory_permissions_mode=None)


class Banner(util_models.TimeStampedModel):
    name = models.CharField(verbose_name='轮播图片名称', max_length=100, blank=True, null=True)
    banner_img = models.ImageField(verbose_name='图片', upload_to='banner_imgs/', storage=BannerStorage())
    seq = models.SmallIntegerField(verbose_name='图片标识')

    class Meta:
        verbose_name_plural = '轮播图片'


# class ArticleType(util_models.TimeStampedModel):
#     name = models.CharField(verbose_name='文章类型', max_length=100, help_text='具体分类')
#
#     class Meta:
#         verbose_name_plural = '文章类型'


class Plate(util_models.TimeStampedModel):
    name = models.CharField(verbose_name='板块名称', max_length=50)
    sum_aticle = models.IntegerField(verbose_name='该板块文章数量', default=0)

    class Meta:
        verbose_name_plural = '区块'


class Article(util_models.TimeStampedModel):
    title = models.CharField(verbose_name='文章标题', max_length=200, help_text='字数不超过200字')
    second_title = models.CharField(verbose_name='文章副标题', max_length=200, help_text='字数200字以下')
    author = models.CharField(verbose_name='作者', max_length=50, help_text='中英文都可以')
    # artice_type = models.ForeignKey(ArticleType, verbose_name='文章类型')
    icon = models.ImageField(verbose_name='文章相关图片')
    content = models.TextField(verbose_name='文章内容')

    plate = models.ForeignKey(Plate, verbose_name='文章所属板块')

    class Meta:
        verbose_name_plural = '文章'


class RecommendUrls(util_models.TimeStampedModel):
    name = models.CharField(verbose_name='链接中文名', max_length=100, blank=True, null=True)
    url = models.CharField(verbose_name='链接地址', max_length=200,)
