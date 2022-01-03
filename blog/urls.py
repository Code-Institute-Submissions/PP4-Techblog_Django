from django.urls import path
# from . import views
from .views import HomePage, ArticleDetailView, AddPostView, EditPostView, DeletePost, AddCategoryView

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', EditPostView.as_view(), name='edit_post'),
    path('article/<int:pk>/remove', DeletePost.as_view(), name='delete_post'),   
]
