from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView

from Post.models import Post, Comment, Reply


class PostListView(ListView):
    model = Post
    template_name = "posts.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "post.html"

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        _pk = self.kwargs["pk"]
        post = Post.objects.get(pk=_pk)
        all_comments = Comment.objects.filter(post=post).order_by("-pk")
        context["all_comments"] = all_comments
        return context

class CommentView(View):
    def post(self, request, **kwargs):
        _comment = request.POST["comment"]
        _pk = self.kwargs["pk"]
        post = Post.objects.get(pk=_pk)
        Comment.objects.create(
            post = post,
            user = request.user,
            comment = _comment
        )
        return redirect(reverse_lazy("post", kwargs={"pk":_pk}))


class ReplyView(View):
    def post(self, request, **kwargs):

        _pk = self.kwargs["pk"]
        _comment = Comment.objects.get(pk=_pk)
        _post = _comment.post.pk
        _reply = request.POST["reply_comment"]
        Reply.objects.create(
            comment = _comment,
            user = request.user,
            reply = _reply
        )
        return redirect(reverse_lazy("post", kwargs={"pk":_post}))