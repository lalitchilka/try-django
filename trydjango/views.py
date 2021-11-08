"""
To return html web page
"""
from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string
import random

def home_view(request):
    random_id = random.randint(1, 4)
    articles_obj = Article.objects.get(id=random_id)
    name = 'Lalit'
    article_title = articles_obj.title
    article_content = articles_obj.content

    article_queryset = Article.objects.all()

    context = {
        "title": article_title,
        "id": random_id,
        "content": article_content,
        "object_list": article_queryset
    }

    HTML_STRING = render_to_string("home-view.html", context=context)
    return HttpResponse(HTML_STRING)
