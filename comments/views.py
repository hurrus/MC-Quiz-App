from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import CommentForm
from .models import Comment


def detail(request):
    comments = Comment.objects.all()
    form = CommentForm()
    return render(request, 'detail.html', {'comments': comments, 'form': form})


def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.created_at = timezone.now()
            comment.save()
            return redirect('detail')
    return redirect('detail')
