# from django.http import HttpResponse
from django.shortcuts import render
# from random import randint
# Create your views here.
from . models import Article # 같은 폴더 안의 models에서 Article을 사용할거야


def index(request):
    # random_number = randint(1,18)
    # return HttpResponse("Hello, word {}".format(random_number))

    # name = "Jay"
    # return render(request, "index.html", {"name" : name})

    article_list = Article.objects.all()
    
    # Article.objects.create(
    #     title = "hello^^",
    #     contents = "test",
    #     view_count = 0
    # )
    ctx = {
        "article_list" : article_list
    }
    return render(request, "index.html", ctx)
