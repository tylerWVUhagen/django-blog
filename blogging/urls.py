from django.urls import path

from blogging.views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name="blog_index"),
    # path('', list_view, name="blog_index"),
    # path('posts/<int:post_id>', detail_view, name="blog_detail")
    path('posts/<int:pk>', PostDetailView.as_view(), name="blog_detail")
]