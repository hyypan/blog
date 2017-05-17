from django import forms
from django.contrib import admin

# Register your models here.
from redactor.widgets import RedactorEditor

from yafish import models as m


@admin.register(m.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('name', 'banner_img', 'seq')


class EntryAdminForm(forms.ModelForm):
    class Meta:
        model = m.Article
        fields = ('title', 'content')
        widgets = {
           'short_text': RedactorEditor(),
        }


@admin.register(m.Article)
class ArticleAdmin(admin.ModelAdmin):
    # form = EntryAdminForm
    list_display = ('title', 'second_title', 'author', 'icon', 'content', 'read_times', 'good_click', 'plate')


@admin.register(m.Plate)
class PlateAdmin(admin.ModelAdmin):
    list_display = ('name', 'sum_aticle')
