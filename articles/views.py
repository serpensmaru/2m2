from django.shortcuts import render

from articles.models import Article, ArticleTags


def articles_list(request):
    template = 'articles/news.html'
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by

    ordering = '-published_at'
    articels = Article.objects.all().order_by(ordering)
    context = {"object_list": articels}

    for article in articels:
        print(article.scopes)

    return render(request, template, context)
