from django.contrib import admin

# Register your models here.
from yafish import models as m


@admin.register(m.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('name', 'banner_img', 'seq')
