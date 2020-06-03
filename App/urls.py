from django.urls import path
from App.views import (AboutView, PostListView, PostDetailView, 
                        PostCreateView, PostUpdateView, 
                        PostDeleteView, DraftPostView, add_comment_to_post, post_publish)


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('about/', AboutView.as_view(), name='about'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/edit', PostDeleteView.as_view(), name='post_delete'),
    path('post/draft/', DraftPostView.as_view(), name='draft_post'),
    path('post/<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
    path('post/<int:pk>/publish/' post_publish, name='post_publish'),
]
 