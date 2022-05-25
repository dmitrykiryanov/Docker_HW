from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, ArticleTag


class ArticleTagInlineFormset(BaseInlineFormSet):
    def clean(self):
        set_is_main = False
        for form in self.forms:
            is_main = form.cleaned_data.get('is_main')
            if is_main:
                if set_is_main:
                    raise ValidationError('Основной раздел может быть только один!')
                set_is_main = True
        if not set_is_main:
            raise ValidationError('Укажите основной раздел!')
        return super().clean()


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    formset = ArticleTagInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTagInline]
    list_display = ['title', 'image', 'text', 'published_at']
    ordering = ['-published_at']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']