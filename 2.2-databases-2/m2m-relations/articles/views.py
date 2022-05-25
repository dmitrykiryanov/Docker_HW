from django.shortcuts import render

from articles.models import Article, Tag


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    articles = Article.objects.all().order_by(ordering)
    tags = Tag.objects.all()
    context = {
        'object_list': articles,
        'tags': tags
    }

    return render(request, template, context)
