from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.


def blogs(request):
    blog_models = Blog.objects.order_by('-date_created')  # [:2]
    context = {
        "content": "This is Blog Section",
        "blog_models": blog_models
    }
    return render(request, "blog_page.html", context)


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        "content":"This is Blog Detail :",
        "blog": blog
    }
    return render(request, "blog_detail.html", context)
