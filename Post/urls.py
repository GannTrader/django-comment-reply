from django.urls import path
from Post.views import PostListView, PostDetailView, CommentView, ReplyView

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post'),

    path('comment/<int:pk>/', CommentView.as_view(), name='comment'),
    path('reply/<int:pk>/', ReplyView.as_view(), name='reply'),
]