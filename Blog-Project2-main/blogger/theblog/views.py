from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

#def home(request):
    #return render(request, "home.html", {})

def LikeView(request, pk):
    post = Post.objects.get(id=pk)
    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False  
    else:
        post.likes.add(request.user.id)
        liked = True
    
    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class ArticleView(DetailView):
    model = Post
    template_name = "detail.html"
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
            liked = True 
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "addpost.html"
    #fields = '__all__'

class AddCategoryView(CreateView):
    model = Category
    
    template_name = "addcategory.html"
    fields = '__all__'

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category = cats)
    return render(request, 'categories.html', {'cats': cats.title(), 'category_posts' : category_posts})

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})

class UpdatePostView(UpdateView):
    model = Post
    template_name = "update.html"
    form_class = EditForm
    #fields = ['title', 'title_tag', 'body']

class DeletPostView(DeleteView):
    model = Post
    template_name = "delete.html"
    success_url = reverse_lazy('home')


