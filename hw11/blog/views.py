from django.shortcuts import render
from django.views.generic import ListView #
from .models import Post

class PostList(ListView): # index.html을 postlist로 바꿔
    model = Post
    template_name = 'blog/index.html'
    ordering = '-pk' # 최신 글 맨 위에 배치
# def index(request):
#     posts = Post.objects.all().order_by('-pk') # order_by 최신 포스트부터 보여 주기
#
#
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts': posts,
#         }
#     )
#
def single_post_page(request,pk):
    posts = Post.objects.get(pk=pk) # order_by 최신 포스트부터 보여 주기


    return render(
        request,
        'blog/single_post_page.html',
        {
            'posts': posts,
        }
    )