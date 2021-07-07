from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_views(request, *args, **kwargs):
    my_dict = {
        'my_text': '"HOW COOL LANGUAGE IT IS."',
        'my_num' : 9453,
        'my_list': ["A", 1, {'home':'HOME'}],
        'my_list2': [1,2,3,4,5,6,7,8,9,10]
    }
    return render(request, "index.html", my_dict)

def about_views(request, *args, **kwargs):
    return render(request, "about.html", {})

def content_views(request, *args, **kwargs):
    return HttpResponse("<h1>this is a content page</h1>")