from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm

def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('success_url')
    else:
        form = CommentForm()
    return render(request, 'create_comment.html', {'form': form})
# Create your views here.


def index(request):
    return HttpResponse("Hello World!")

