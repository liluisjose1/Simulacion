from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here.
from django.shortcuts import render, get_object_or_404
def index(request):
    """
    View function for home page of site.
    """
    # cantidad de objetos del modelo post
    num_post=Post.objects.all().count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_post':num_post},
    )
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'post_list': posts})
#Agregar un form
from .forms import PostForm
from django.shortcuts import redirect
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
