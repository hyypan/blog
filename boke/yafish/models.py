from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from model_utils import models as util_models
from django.db import models
from redactor.fields import RedactorField

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
    name = models.CharField(verbose_name='板块名称', choices=
                            (('python', 'python'),
                             ('vue', 'vue'),
                             ('linux', 'linux'),
                             ('docker', 'docker'),
                             ('ansible', 'ansible'),
                             ('nginx', 'nginx'),
                             ('others', 'others'))
                            , max_length=50)
    sum_aticle = models.IntegerField(verbose_name='该板块文章数量', default=0)

    class Meta:
        verbose_name_plural = '区块'

    def __str__(self):
        return self.name

class Article(util_models.TimeStampedModel):
    title = models.CharField(verbose_name='文章标题', max_length=200, help_text='字数不超过200字')
    second_title = models.CharField(verbose_name='文章副标题', max_length=200, blank=True, null=True, help_text='字数200字以下')
    author = models.CharField(verbose_name='作者', max_length=50, help_text='中英文都可以')
    icon = models.ImageField(verbose_name='文章相关图片', blank=True, default='admin/img', upload_to='banner_imgs/',
                             storage=BannerStorage())
    content = RedactorField(verbose_name='文章内容')
    read_times = models.IntegerField(verbose_name='阅读数', default=0)
    good_click = models.IntegerField(verbose_name='点赞次数', default=0)
    plate = models.ForeignKey(Plate, verbose_name='文章所属板块')

    class Meta:
        verbose_name_plural = '文章'


class Commends(util_models.TimeStampedModel):
    user = models.ForeignKey(User, verbose_name='用户')
    content = models.TextField(verbose_name='用户评论内容')
    article = models.ForeignKey(Article, verbose_name='所评论的文章')

    class Meta:
        verbose_name_plural = '文章评论'


class RecommendUrls(util_models.TimeStampedModel):
    name = models.CharField(verbose_name='链接中文名', max_length=100, blank=True, null=True)
    url = models.CharField(verbose_name='链接地址', max_length=200,)

    class Meta:
        verbose_name_plural = '推荐链接'
