from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post
#

# Create your views here.
def post_page(request):
    posts = Post.objects.all().order_by('-created_at')
    per_page = request.GET.get('per_page', 3)
    try:
        per_page = int(per_page)
    except ValueError:
        per_page = 3
    paginator = Paginator(posts, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return  render(request, 'post_page.html', {'page_obj': page_obj, 'per_page': per_page})