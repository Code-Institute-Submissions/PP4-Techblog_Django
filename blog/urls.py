from django.urls import path
# from . import views
from .views import HomePage, ArticleDetailView, AddPostView, EditPostView

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', EditPostView.as_view(), name='edit_post'),
]
