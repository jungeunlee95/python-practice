# from django.http import HttpResponse
from django.shortcuts import render
# from random import randint
# Create your views here.



def index(request):
    # random_number = randint(1,18)
    # return HttpResponse("Hello, word {}".format(random_number))
    name = "Jay"
    return render(request, "index.html", {"name" : name})
