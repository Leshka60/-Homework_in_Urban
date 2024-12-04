from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post


# def post_list(request):
#     posts = Post.objects.all().order_by('-created_at')
#     paginator = Paginator(posts, 3)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return  render(request, 'post_plist.html', {'page_obj': page_obj})
