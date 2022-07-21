from . import views
from django.urls import path
from .views import HomeView, ArticleView, AddPostView, UpdatePostView, DeletPostView,  AddCategoryView, CategoryView, CategoryListView, LikeView

urlpatterns = [
   #path('', views.home, name = "home"),
   path('', HomeView.as_view(), name = "home"),
   path('article/<int:pk>', ArticleView.as_view(), name = "detail"),
   path('addpost/', AddPostView.as_view(), name = "Add"),
   path('updateview/<int:pk>', UpdatePostView.as_view(), name = "Update" ),
   path('delete//<int:pk>', DeletPostView.as_view(), name = "Delete"),
   path('addcategory/',  AddCategoryView.as_view(), name ="category"),
   path('category/<str:cats>/', CategoryView, name = 'Category'),
   path('category_list/', CategoryListView, name = 'Category_list'),
   path('like/<int:pk>', LikeView, name = 'like_post'),


]