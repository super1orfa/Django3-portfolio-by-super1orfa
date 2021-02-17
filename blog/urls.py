from django.urls import path, include
from .views import blogs, blog_detail

app_name = "blog"

urlpatterns = [
    path('', blogs, name="blogs"),
    path('<int:blog_id>/', blog_detail, name="blog_detail")
]
